# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template.context import RequestContext
from django.template import Template


class FirstLoginMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated():
            if 'check' not in request.session:
                request.session['check'] = True
                if request.user.perfilusuario.is_first_login:
                    return redirect(reverse('reset-senha'))


class CachedTemplateMiddleware(object):

    def process_response(self, request, response):
        if request.method == 'GET' and response['content-type'].startswith('text/html'):
            template = Template(response.content)
            response.content = template.render(RequestContext(request))
        return response
