from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as gt
from django import forms


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default='', verbose_name=gt('username'))
    first_name = models.CharField(max_length=50, default='', verbose_name=gt('first_name'))
    last_name = models.CharField(max_length=50, default='', verbose_name=gt('last_name'))
    city = models.CharField(max_length=50, default='', verbose_name=gt('city'))
    phone = models.CharField(max_length=30, default='', verbose_name=gt('phone'))
    is_verified = models.BooleanField()
    news_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class News(models.Model):
    STATUS_CHOICES = [
        ('d', gt('draft')),
        ('a', gt('archive')),
        ('p', gt('post')),
    ]
    title = models.CharField(max_length=200, default='', verbose_name=gt('title'))
    author = models.ForeignKey(get_user_model(), default=None, null=True,
                             on_delete=models.CASCADE, verbose_name=gt('author'), blank=True)
    description = models.CharField(max_length=1000, default='', verbose_name=gt('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=gt('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=gt('updated_at'))
    tag = models.CharField(max_length=50, default='', verbose_name=gt('tag'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d', verbose_name=gt('status'))
    admin_comment = models.CharField(max_length=200, default='', verbose_name=gt('admin_comment'))
    age_rate = models.CharField(max_length=5, default='', verbose_name=gt('age_rate'))
    # image = models.FileField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'media/')

    def __str__(self):
        return self.news.title


class Comment(models.Model):
    author = models.CharField(max_length=200, default='', verbose_name='автор', blank=True)
    user = models.ForeignKey(get_user_model(), default=None, null=True,
                             on_delete=models.CASCADE, verbose_name='пользователь', blank=True)
    text = models.CharField(max_length=1000, default='', verbose_name='текст')
    news = models.ForeignKey('News', default=None, null=True,
                             on_delete=models.CASCADE, verbose_name='новость')

    def __str__(self):
        return self.author
