# Generated by Django 3.2.4 on 2021-09-18 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210811_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles_autor',
            fields=[
            ],
            options={
                'ordering': ['autor'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('blog.blog_articles',),
        ),
    ]
