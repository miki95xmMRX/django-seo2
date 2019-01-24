from __future__ import unicode_literals

from django.apps.config import AppConfig

from djangoseo.models import setup


class SeoConfig(AppConfig):
    name = 'djangoseo'
    verbose_name = 'djangoseo'

    def ready(self):
        setup()
