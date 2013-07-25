# coding: utf-8

from django.conf import settings
from django.contrib.admindocs.views import simplify_regex
from django.core.exceptions import ViewDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver

from random import randint

def to_hex(c):
    r = hex(c[0])[2:].zfill(2)[:2]
    g = hex(c[1])[2:].zfill(2)[:2]
    b = hex(c[2])[2:].zfill(2)[:2]
    return [r, g, b]


def get_view_func_regex_url_name(urlpatterns, admin=False):
    """
        Retorna uma lista de tuplas com 3 elementos (view, regex, nome da url)
        de uma lista de urlpatterns.
    """
    views = []
    def urls_recur(urlpatterns, depth=''):
        for patt in urlpatterns:
            regex_pattern = patt.regex.pattern
            if not admin:
                if regex_pattern.startswith('^admin/'):
                    continue
            if isinstance(patt, RegexURLPattern):
                try:
                    views.append((patt.callback, depth + regex_pattern, patt.name))
                except ViewDoesNotExist:
                    continue
            elif hasattr(patt, '_get_callback'):
                try:
                    views.append((patt._get_callback(), depth + regex_pattern, patt.name))
                except ViewDoesNotExist:
                    continue
            elif isinstance(patt, RegexURLResolver):
                try:
                    patterns = patt.url_patterns
                except ImportError:
                    continue
                urls_recur(patterns, depth + regex_pattern)
            elif hasattr(patt, 'url_patterns'):
                try:
                    patterns = patt.url_patterns
                except ImportError:
                    continue
                urls_recur(patterns, depth + regex_pattern)
    urls_recur(urlpatterns)
    return views


def views_to_graph(views, diag=True, colorful=True, with_label=True):
    """
        Retorna um grafo na linguagem dot a partir 
        do retorno da função get_view_func_regex_url_name
    """
    graph = 'blockdiag' if diag else 'graph'
    urls, colors = [], []
    def get_color():
        while True:
            color = to_hex((randint(5, 200), randint(5, 200), randint(5, 200)))
            if color in colors:
                continue
            colors.append(color)
            return color

    for index, (v, r, n) in enumerate(views):
        if colorful:
            if index > 0:
                color = 'color="#%s"' % ''.join(get_color())
            else:
                color = 'color="#ffffff"'

        if with_label:
            if hasattr(v, '__name__'):
                label = v.__name__
            else:
                label = v.__class__.__name__
            label = 'label="%s"' % label

        if not colorful and not with_label:
            opts = ''
        elif colorful and not with_label:
            opts = ' [%s]' % color
        elif with_label and not colorful:
            opts = ' [%s]' % label
        else:
            opts = ' [%s, %s]' % (color, label)

        u = '"/%s' % simplify_regex(r).replace('/', '" -> "')
        if u.endswith(' -> "'):
            u = u[0:-5] + '%s;' % opts
        else:
            u += '"%s;' % opts 

        urls.append("    %s" % u)
    return '%s {\n%s\n}' % (graph, '\n'.join(urls))


class Command(BaseCommand):

    def handle(self, *args, **options):
        if settings.ADMIN_FOR:
            settings_modules = [__import__(m, {}, {}, ['']) for m in settings.ADMIN_FOR]
        else:
            settings_modules = [settings]

        for settings_mod in settings_modules:
            try:
                urlconf = __import__(settings_mod.ROOT_URLCONF, {}, {}, [''])
            except:
                continue

        print views_to_graph(get_view_func_regex_url_name(urlconf.urlpatterns))