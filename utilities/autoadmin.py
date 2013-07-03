from django.conf import settings
from django.db.models import get_models
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin


def autodiscover():
    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        if module_has_submodule(mod, 'models'):
            if not module_has_submodule(mod, 'admin'):
                models = import_module('%s.models' % app)
                for model in get_models(models):
                    try:
                        admin.site.register(model)
                    except AlreadyRegistered:
                        pass
            else:
                import_module('%s.admin' % app)
