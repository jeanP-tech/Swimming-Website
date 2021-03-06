# Generated by Django 2.2.4 on 2019-09-17 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_name', models.CharField(default='', max_length=30)),
                ('city', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='swimapp.City')),
            ],
        ),
        migrations.CreateModel(
            name='TimeInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=1)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swimapp.Pool')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('week', models.CharField(choices=[('WEEK', 'Weekdays'), ('WEEKENDS', 'Weekends')], default='WEEK', max_length=10)),
                ('registered', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=1)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swimapp.Pool')),
            ],
        ),
    ]
