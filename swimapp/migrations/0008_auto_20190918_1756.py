# Generated by Django 2.2.4 on 2019-09-18 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0007_auto_20190917_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeinterval',
            name='time',
        ),
        migrations.RemoveField(
            model_name='timeinterval',
            name='time_name',
        ),
    ]