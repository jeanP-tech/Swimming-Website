# Generated by Django 2.2.4 on 2019-09-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0043_remove_timeinterval_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeinterval',
            name='times',
            field=models.IntegerField(default=''),
        ),
    ]
