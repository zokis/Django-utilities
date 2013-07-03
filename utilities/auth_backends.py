# coding: utf-8
from django.contrib.auth.models import User
from django.db.models import Q


class EmailBackend(object):
    def authenticate(self, username='', password=''):
        q = Q(username=username)
        if '@' in username:
            q = Q(email=username)
        try:
            user = User.objects.get(q)

            if user.check_password(password):
                return user
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None

    supports_anonymous_user = False
    supports_inactive_user = False
    supports_object_permissions = False
