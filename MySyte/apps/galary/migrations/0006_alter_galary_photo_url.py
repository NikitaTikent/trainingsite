# Generated by Django 3.2.4 on 2021-08-12 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galary', '0005_auto_20210811_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galary',
            name='photo_url',
            field=models.TextField(validators=[django.core.validators.URLValidator(schemes=['http', 'https'])], verbose_name='Ссылка на фотографию'),
        ),
    ]