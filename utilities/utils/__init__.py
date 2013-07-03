# coding: utf-8
from django.conf import settings


from datetime import date
import time


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
