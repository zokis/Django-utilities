# coding: utf-8
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from datetime import date
import time


def get_paginator_context(objects, request, n_pages=10):
    paginator = Paginator(objects, n_pages)
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return {
        'object_list': object_list,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': object_list,
        'paginator': paginator
    }


def get_model_attr(ins_obj, attr):
    for field in attr.split('__'):
        ins_obj = getattr(ins_obj, field)
    return ins_obj


def get_next_or_previous(ins_obj=None, next=True, qs=None):
    model = type(ins_obj)
    if qs is None:
        qs = model.objects
    if next is False:
        qs = qs.reverse()
        ascending = True
    else:
        ascending = False
    list_q = []
    prev_fields = []
    if model._meta.ordering:
        ordering = list(model._meta.ordering).append('pk')
    else:
        ordering = ['pk']
    for field in ordering:
        if field.startswith('-'):
            field = field[1:]
        q_kwargs = dict((pref_field, get_model_attr(
            ins_obj, pref_field)) for pref_field in prev_fields)
        key = "%s__%s" % (field, 'lg' if ascending else 'gt')
        q_kwargs[key] = get_model_attr(ins_obj, field)
        list_q.append(Q(**q_kwargs))
        prev_fields.append(field)
    try:
        q = Q()
        for curr_q in list_q:
            q = q | curr_q
        return qs.filter(q)[0]
    except IndexError:
        return qs.none()


DATE_FTMS = ('%d/%m/%Y', '%d/%m/%y', '%d-%m-%Y', '%Y-%m-%d',)


def parse_date(value, formats=DATE_FTMS):
    date_value = None
    for fmt in formats:
        try:
            date_value = date(*time.strptime(value, fmt)[:3])
            break
        except ValueError:
            pass
    return date_value


def get_years(year=None):
    if year is None:
        year = settings.START_YEAR
    return range(year, date.today().year + 1)


def converte_unicode(v):
    if isinstance(v, basestring):
        try:
            v = unicode(v, 'utf-8')
        except UnicodeDecodeError:
            try:
                v = unicode(v, 'latin-1')
            except UnicodeDecodeError:
                pass
    return v
