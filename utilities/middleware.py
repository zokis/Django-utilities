# coding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class FirstLoginMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            if 'check' not in request.session:
                request.session['check'] = True
                if request.user.perfilusuario.is_first_login:
                    return redirect(reverse('reset-senha'))
