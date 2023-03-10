# Generated by Django 4.1.6 on 2023-02-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeSantiago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('free_bikes', models.PositiveIntegerField()),
                ('empty_slots', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10000)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('typology', models.CharField(max_length=200)),
                ('holder', models.CharField(max_length=200)),
                ('investment', models.CharField(max_length=200)),
                ('date_presentation', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]
