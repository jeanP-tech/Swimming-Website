# Generated by Django 2.0.13 on 2019-08-07 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swimapp', '0004_auto_20190806_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('pool', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='swimapp.Pool')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('pool', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='swimapp.Pool')),
            ],
        ),
    ]
