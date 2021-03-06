# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_for_loan', models.BooleanField(default=0)),
                ('car_company_name', models.CharField(max_length=200)),
                ('car_vin', models.IntegerField(unique=True)),
                ('car_category', models.CharField(max_length=100)),
                ('car_type', models.BooleanField(default=1)),
                ('car_accident', models.BooleanField(default=0)),
                ('car_make', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_year', models.IntegerField(default=0)),
                ('car_km', models.IntegerField(default=0)),
                ('car_body', models.CharField(max_length=100)),
                ('car_transmission', models.CharField(max_length=100)),
                ('car_fuel', models.CharField(max_length=100)),
                ('car_door', models.IntegerField()),
                ('car_color', models.CharField(max_length=100)),
                ('car_engine_size', models.IntegerField(default=0)),
                ('car_price', models.IntegerField(default=0)),
                ('car_vnumber', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='CarCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_company_name', models.CharField(max_length=200)),
                ('car_company_inn', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['car_company_name'],
                'db_table': 'car_company',
            },
        ),
        migrations.CreateModel(
            name='CarCompanyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_company_group_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['car_company_group_name'],
                'db_table': 'car_company_group',
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image_uuid', models.UUIDField(unique=True)),
                ('car_image_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car')),
            ],
            options={
                'ordering': ['car_image_car'],
                'db_table': 'car_image',
            },
        ),
        migrations.AddField(
            model_name='carcompany',
            name='car_company_car_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_company_car_group_key', to='car.CarCompanyGroup'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_car_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.CarCompany'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_car_company_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.CarCompanyGroup'),
        ),
    ]
