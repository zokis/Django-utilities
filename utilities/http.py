# coding: utf-8
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from utilities.utils import instance_to_json


class HttpResponseNotAuthorized(HttpResponse):
    status_code = 401

    def __init__(self, username, password):
        super(HttpResponse, self).__init__()
        self['WWW-Authenticate'] = (
            'Basic realm="%s"' %
                (
                    "%s:%s" % (username, password)
                ).encode('base64', 'strict')
            )


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
