# Generated by Django 3.2.4 on 2021-08-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('photo_url', models.TextField(verbose_name='Ссылка на фотографию')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Галерея',
            },
        ),
    ]
