# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.

class CarCompanyGroup(models.Model):
	class Meta():
		db_table = "car_company_group"
		ordering = ['car_company_group_name']

	car_company_group_name = models.CharField(
		max_length=200,
		blank=False,
		null=False,
	)


class CarCompany(models.Model):
	class Meta():
		db_table = "car_company"
		ordering = ['car_company_name']

	car_company_car_group = models.ForeignKey(
		CarCompanyGroup,
		related_name="car_company_car_group_key",
		blank=False,
		null=False,
	)

	car_company_name = models.CharField(
		max_length=200,
		blank=False,
		null=False,
	)
	car_company_inn = models.IntegerField(
		unique=True,
		blank=False,
		null=False,
	)



class Car(models.Model):
	class Meta():
		db_table = "car"
		ordering = ['-id']

	car_for_loan = models.BooleanField(
		default=0,
		blank=False,
		null=False,
	)
	car_car_company_group = models.ForeignKey(
		CarCompanyGroup,
		blank=False,
		null=False,
	)
	car_car_company = models.ForeignKey(
		CarCompany,
		blank=False,
		null=False,
	)
	car_vin = models.CharField(
		max_length=1000,
		unique=True,
		blank=False,
		null=False,
	)
	car_category = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_type = models.BooleanField(
		default=1,
		blank=False,
		null=False,
	)
	car_accident = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_make = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_model = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_year = models.IntegerField(
		default=0,
		blank=False,
		null=False,
	)
	car_km = models.CharField(
		max_length=1000,
		blank=False,
		null=False,
	)
	car_body = models.CharField(
		max_length=100,
		blank=False,
	)
	car_transmission = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_fuel = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_door = models.IntegerField(
		blank=False,
		null=False,
	)
	car_color = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_engine_size = models.IntegerField(
		default=0,
		blank=False,
		null=False,
	)
	car_price = models.IntegerField(
		default=0,
		blank=False,
		null=False,
	)
	car_vnumber = models.CharField(
		max_length=1000,
		blank=False,
	)
	car_date = models.DateTimeField(
		auto_now_add=True,
		blank=False,
		null=False
	)


class CarImage(models.Model):
	class Meta():
		db_table = "car_image"
		ordering = ['car_image_car']

	car_image_uuid = models.UUIDField(
		default=uuid.uuid4,
		unique=True,
		editable=False,
		blank=False,
		null=False,
	)

	car_image_url = models.CharField(
		max_length = 200,
		blank=False,
		null=False,
	)

	car_image_car = models.ForeignKey(
		Car,
		related_name="car_image_car_key",
		blank=False,
		null=False,
	)