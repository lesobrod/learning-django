# Generated by Django 4.0.3 on 2022-03-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0016_auto_20220321_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('a', 'archive'), ('p', 'post')], default='d', max_length=1, verbose_name='status'),
        ),
    ]
