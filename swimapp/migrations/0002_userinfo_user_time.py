# Generated by Django 2.2.4 on 2019-08-23 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 24, 0, 5, 38, 397581)),
        ),
    ]
