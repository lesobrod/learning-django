# Generated by Django 4.0.3 on 2022-04-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0017_alter_news_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
