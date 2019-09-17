# Generated by Django 2.2.4 on 2019-09-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0002_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeinterval',
            name='time',
            field=models.IntegerField(choices=[(3, '3시간'), (7, '7시간'), (12, '12시간'), (24, '24시간')], default=0),
        ),
        migrations.AddField(
            model_name='timeinterval',
            name='time_name',
            field=models.CharField(default='', max_length=10),
        ),
    ]
