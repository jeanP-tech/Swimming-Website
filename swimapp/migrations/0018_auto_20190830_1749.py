# Generated by Django 2.2.4 on 2019-08-30 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0017_auto_20190830_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 30, 17, 49, 10, 574182)),
        ),
    ]
