from django.db import models
from django.http import Http404


class BaseManager(models.Manager):

    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None

    def get_or_404(self, *args, **kwargs):
        obj = self.get_or_none(*args, **kwargs)
        if obj is None:
            raise Http404
        return obj
