# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from models import CarCompanyGroup, CarCompany, Car, CarImage


class CarCompanyGroupForm(forms.ModelForm):
	class Meta:
		model = CarCompanyGroup
		exclude = (
			'car_company_group_name',
		)


class CarCompanyForm(forms.ModelForm):
	class Meta:
		model = CarCompany
		exclude = (
			'car_company_car_group',
			'car_company_name',
			'car_company_inn',
		)


class CarForm(forms.ModelForm):
	class Meta:
		model = Car
		exclude = (
			'car_for_loan',
			'car_car_company_group',
			'car_car_company',
			'car_vin',
			'car_category',
			'car_type',
			'car_accident',
			'car_make',
			'car_model',
			'car_year',
			'car_km',
			'car_body',
			'car_transmission',
			'car_fuel',
			'car_door',
			'car_color',
			'car_engine_size',
			'car_price',
			'car_vnumber',
		)


class CarImageForm(forms.ModelForm):
	class Meta:
		model = CarImage
		exclude = (
			'car_image_uuid',
			'car_image_url',
			'car_image_car',
		)