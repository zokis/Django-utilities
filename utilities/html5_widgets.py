# coding: utf-8
from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput


class EmailInput(TextInput):
    input_type = 'email'


class NumberInput(TextInput):
    input_type = 'number'


class TelephoneInput(TextInput):
    input_type = 'tel'


class DateInput(DateInput):
    input_type = 'date'


class DateTimeInput(DateTimeInput):
    input_type = 'datetime'


class TimeInput(TimeInput):
    input_type = 'time'
