# Generated by Django 3.2.4 on 2021-09-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galary', '0007_alter_galary_photo_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galary',
            options={'ordering': ['order', 'autor'], 'verbose_name': 'Галерея', 'verbose_name_plural': 'Галерея'},
        ),
        migrations.AddField(
            model_name='galary',
            name='order',
            field=models.SmallIntegerField(db_index=True, default=0),
        ),
    ]
