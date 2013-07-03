from django.forms.fields import Field
from django.core.validators import EMPTY_VALUES
from django.utils.encoding import smart_unicode
from django.forms import ValidationError
import re


class BRPhoneNumberField(Field):

    def clean(self, value):
        super(BRPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''
        value = re.sub('(\(|\)|\s+)', '', smart_unicode(value))
        m = re.compile(
            r'^(\d{2})[-\.]?((\d{5})|(\d{4}))[-\.]?(\d{4})$').search(value)
        if m:
            gs = m.groups()
            return u'%s-%s-%s' % (gs[0], gs[1], gs[4])
        raise ValidationError(u'Formato Errado')
