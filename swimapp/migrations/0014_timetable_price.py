# Generated by Django 2.2.4 on 2019-10-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0013_remove_price_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='price',
            field=models.ManyToManyField(to='swimapp.Price'),
        ),
    ]
