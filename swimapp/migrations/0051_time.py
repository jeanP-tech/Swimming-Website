# Generated by Django 2.2.4 on 2019-09-17 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0050_remove_timeinterval_times'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
            ],
        ),
    ]
