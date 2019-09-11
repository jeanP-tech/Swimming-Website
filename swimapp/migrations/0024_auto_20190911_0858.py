# Generated by Django 2.2.4 on 2019-09-10 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0023_auto_20190831_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='age',
        ),
        migrations.AddField(
            model_name='price',
            name='registered',
            field=models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=1),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 11, 8, 58, 48, 13684)),
        ),
    ]
