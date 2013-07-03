# -*- coding: utf-8 -*-
from django import forms
from django.contrib.contenttypes.models import ContentType


class GenericRelationsForm(forms.ModelForm):

    '''
    example:
    class FotoForm(GenericRelationsForm):
        class Meta:
            model = Foto
            exclude = ['content_type', 'object_id']
    '''

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('object', None)
        super(GenericRelationsForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kargs):
        is_new = self.instance.pk is None
        commit = kargs.pop('commit', True)
        kargs.update({'commit': False})
        instance = super(GenericRelationsForm, self).save(*args, **kargs)
        if is_new:
            instance.object_id = self.obj.pk
            instance.content_type = ContentType.objects.get_for_model(self.obj)
        if commit:
            instance.save()
        return instance
