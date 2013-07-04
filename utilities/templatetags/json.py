# coding: utf-8
from django import template

from utilies.utils import instance_to_json

from json import dumps

register = template.Library()


def instance_to_json_filter(instance, *args):
    return instance_to_json(instance, exclude=args)

register.filter('instance_to_json', instance_to_json_filter)
register.filter('json_dumps', dumps)
