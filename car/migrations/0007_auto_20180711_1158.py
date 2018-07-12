# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_car_car_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='car_image_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
