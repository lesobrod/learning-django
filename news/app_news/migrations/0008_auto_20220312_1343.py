# Generated by Django 2.2 on 2022-03-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0007_auto_20220309_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=50, verbose_name='имя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=50, verbose_name='фамилия'),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=50, verbose_name='ник'),
        ),
    ]
