# coding: utf-8
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.sites.models import Site
from django.http import HttpResponse

from utilities.utils import instance_to_json


REALM = settings.get('SOCIAL_API_REALM', Site.objects.get_current().name)


class HttpResponseNotAuthorized(HttpResponse):
    status_code = 401

    def __init__(self, redirect_to):
        super(HttpResponse, self).__init__()
        self.update('WWW-Authenticate', ('Basic realm="%s"' % REALM))


class InstanceJsonResponse(HttpResponse):

    def __init__(self, instance, fields=None, exclude=None):
        super(InstanceJsonResponse, self).__init__(
            instance_to_json(instance, fields=fields, exclude=exclude),
            content_type='application/json')


class JsonResponse(HttpResponse):

    def __init__(self, obj):
        encoder = DjangoJSONEncoder(
            encoding='utf-8', ensure_ascii=False, sort_keys=False, indent=1)
        super(JsonResponse, self).__init__(
            encoder.encode(obj),
            content_type='application/json')
