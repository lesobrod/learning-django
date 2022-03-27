from django.apps import AppConfig
from django.utils.translation import  gettext_lazy as gt


class AppNewsConfig(AppConfig):
    name = 'app_news'
    verbose_name = gt('news')
