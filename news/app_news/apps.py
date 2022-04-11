from django.apps import AppConfig
from django.utils.translation import  gettext_lazy as gt


class AppNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_news'
    verbose_name = gt('news')

    def ready(self):
        from . import signals
