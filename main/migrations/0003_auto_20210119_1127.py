# Generated by Django 3.1.2 on 2021-01-19 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210118_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='favorite',
            new_name='popular',
        ),
    ]
