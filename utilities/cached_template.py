from django.template.context import RequestContext
from django.template import Template


class CachedTemplateMiddleware(object):
    def process_response(self, request, response):
        if request.method == 'GET' and response['content-type'].startswith('text/html'):
            template = Template(response.content)
            response.content = template.render(RequestContext(request))
        return response
