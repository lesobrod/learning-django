# Generated by Django 2.2 on 2022-02-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_auto_20220221_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('d', 'Черновик'), ('a', 'Архив'), ('p', 'Опубликовано')], default='d', max_length=1, verbose_name='статус'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
