# Generated by Django 2.2.4 on 2019-11-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0021_auto_20191010_0520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='price',
        ),
        migrations.AddField(
            model_name='pool',
            name='price',
            field=models.IntegerField(choices=[(3000, '회원(주중)'), (3500, '비회원(주중)'), (3500, '회원(주말)'), (4100, '비회원(주말)')], default=3000),
        ),
    ]
