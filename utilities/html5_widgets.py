# coding: utf-8
from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput, NumberInput, URLInput

# from http://www.w3schools.com/html/html5_form_input_types.asp


class ColorInput(TextInput):
    '''
        Opera - ok
        Safari
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'color'


class DateInput(DateInput):
    '''
        Opera - ok
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'date'


class DateTimeInput(DateTimeInput):
    '''
        Opera - ok
        Safari - ok
        Chrome
        Firefox
        Internet Explorer
    '''
    input_type = 'datetime'


class DateTimeLocalInput(DateTimeInput):
    '''
        Opera - ok
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'datetime-local'


class EmailInput(TextInput):
    '''
        Opera - ok
        Safari
        Chrome - ok
        Firefox - ok
        Internet Explorer - ok
    '''
    input_type = 'email'


class MonthInput(TextInput):
    '''
        Opera - ok
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'month'


class NumberInput(NumberInput):
    '''
        Opera - ok
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer - ok
    '''
    input_type = 'number'

    def __init__(self, min_n=1, max_n=None, attrs=None):
        attrs_default = {}
        if min_n:
            attrs_default['min'] = min_n
        if max_n:
            attrs_default['max'] = max_n
        if attrs:
            attrs_default.update(attrs)
        super(NumberInput, self).__init__(attrs=attrs_default)


class RangeInput(TextInput):
    '''
        Opera - ok
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'range'

    def __init__(self, min_n=1, max_n=None, attrs=None):
        attrs_default = {}
        if min_n:
            attrs_default['min'] = min_n
        if max_n:
            attrs_default['max'] = max_n
        if attrs:
            attrs_default.update(attrs)
        super(RangeInput, self).__init__(attrs=attrs_default)


class SearchInput(TextInput):
    '''
        Opera
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'search'


class TelInput(TextInput):
    '''
        Opera
        Safari
        Chrome
        Firefox
        Internet Explorer
    '''
    input_type = 'tel'


class TimeInput(TimeInput):
    '''
        Opera - ok
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'time'


class URLInput(URLInput):
    '''
        Opera - ok
        Safari
        Chrome - ok
        Firefox - ok
        Internet Explorer - ok
    '''
    input_type = 'url'


class WeekInput(TextInput):
    '''
        Opera - ok
        Safari - ok
        Chrome - ok
        Firefox
        Internet Explorer
    '''
    input_type = 'week'
