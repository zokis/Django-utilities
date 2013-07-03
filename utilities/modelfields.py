from django.contrib.db import models
from django.core.exceptions import ValidationError

from .widgets import TelefoneWidget

import re


class TelefoneField(models.CharField):

    def formfield(self, *args, **kwargs):
        kwargs['widget'] = TelefoneWidget()
        return super(TelefoneField, self).formfield(*args, **kwargs)

    def clean(self, value, model_instance):
        value = value.replace(' ', '')
        regex = re.compile(
            r'^(\d{2})-((\d{5})|(\d{4}))-(\d{4})$', re.IGNORECASE | re.UNICODE)

        if len(regex.findall(value)) != 1:
            raise ValidationError(u'Telefone %s inválido' % value)

        return super(TelefoneField, self).clean(value, model_instance)
