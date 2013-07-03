from django.utils.numberformat import format
from django import template

register = template.Library()


@register.filter
def float_format_br(number, decimal_pos=2):
    if number is None:
        return ''
    return format(number, decimal_sep=',', decimal_pos=decimal_pos, grouping=3, thousand_sep='.', force_grouping=3)


@register.filter
def integer_format_br(number):
    if number is None:
        return ''
    number = int(number)
    return format(number, decimal_sep='', decimal_pos=0, grouping=3, thousand_sep='.', force_grouping=3)


@register.filter
def monetary_format_br(number):
    if number is None:
        return ''
    number = float(number)
    return format(number, decimal_sep=',', decimal_pos=2, grouping=3, thousand_sep='.', force_grouping=3)
