# Generated by Django 2.2.4 on 2019-08-24 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0004_auto_20190824_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 24, 23, 23, 42, 312800)),
        ),
    ]
