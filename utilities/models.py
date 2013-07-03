# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class UserDateAdd(models.Model):
    user_add = models.ForeignKey(User,
                                 related_name='%(app_label)s_%(class)s_created_by',
                                 blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserDateUpd(models.Model):
    user_upd = models.ForeignKey(User,
                                 related_name='%(app_label)s_%(class)s_modified_by',
                                 blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
