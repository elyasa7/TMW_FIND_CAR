# -*- coding: utf-8 -*-
# encoding=utf8

from __future__ import unicode_literals
import uuid
#import boto3
#from botocore.client import Config
from datetime import datetime
from django.shortcuts import render
import json
from car.models import *
from car.forms import *
from django.core.paginator import Paginator
from django.http.response import HttpResponse, HttpResponseRedirect
import xlwt

# Create your views here.

args = {}


def car_list(request, page_number=1):
	if len(str(request.COOKIES.get('order_cars_by', ''))) >= 1:
		order_cars_by = request.COOKIES.get('order_cars_by')
	else:
		order_cars_by = 'id'

	if len(str(request.COOKIES.get('show_cars_by', ''))) >= 1:
		show_cars_by = request.COOKIES.get('show_cars_by')
	else:
		show_cars_by = 20

	all_cars = Car.objects.all().order_by(order_cars_by)
	if len(str(request.COOKIES.get('filter_vin_code', ''))) >= 1:
		all_cars = all_cars.filter(car_vin__contains=request.COOKIES.get('filter_vin_code'))
	if len(str(request.COOKIES.get('filter_car_date', ''))) >= 1:
		all_cars = all_cars.filter(car_date__contains=request.COOKIES.get('filter_car_date'))
	if len(str(request.COOKIES.get('filter_car_for_loan', ''))) >= 1:
		all_cars = all_cars.filter(car_for_loan=request.COOKIES.get('filter_car_for_loan'))
	cars_page = Paginator(all_cars, show_cars_by)
	args['cars'] = cars_page.page(page_number)
	args['all_cars'] = Car.objects.all().order_by(order_cars_by)
	args['title'] = u"Список автомобилей"
	args['show_cars_by'] = show_cars_by
	args['cookies'] = request.COOKIES
	return render(request, 'car_list.html', args)


def car_profile(request, car_id):
	try:
		args['car'] = Car.objects.get(id__exact=car_id)
	except:
		args['car'] = None
	if args['car'] is not None:
		args['title'] = u"Подробности автомобиля"
		return render(request, 'car_profile.html', args)
	else:
		return HttpResponseRedirect('/')


def car_add(request):
	args['title'] = u"Загрузить новые автомобили"
	return render(request, 'car_add.html', args)


def car_change_show_count(request):
	if request.POST:
		show_count = request.POST.get('show_by_count', None)
		if show_count is not None:
			response = HttpResponseRedirect('/car/list/')
			response.set_cookie('show_cars_by', show_count)
			return response
		else:
			return HttpResponseRedirect('/car/list/')
	else:
		return HttpResponseRedirect('/car/list/')


def car_change_order_by(request):
	if request.POST:
		order_by = request.POST.get('car_change_order_by', None)

		try:
			current_order = request.COOKIES['order_cars_by']
		except:
			current_order = None
		if order_by is not None:
			response = HttpResponseRedirect('/car/list/')
			if order_by == current_order:
				response.set_cookie('order_cars_by', str('-') + str(order_by))
				return response
			else:
				response.set_cookie('order_cars_by', str(order_by))
				return response
		else:
			return HttpResponseRedirect('/car/list/')
	else:
		return HttpResponseRedirect('/car/list/')


def car_filter_set(request):
	if request.POST:
		vin_code = request.POST.get('car_vin', None)
		car_date = request.POST.get('car_date', None)
		car_for_loan = request.POST.get('car_for_loan', None)

		response = HttpResponseRedirect('/car/list/')

		if vin_code is not None:
			try:
				response.set_cookie('filter_vin_code', vin_code)
			except:
				pass
		else:
			try:
				response.delete_cookie('filter_vin_code', None, -1000)
			except:
				pass

		if car_date is not None:
			try:
				response.set_cookie('filter_car_date', car_date)
			except:
				pass
		else:
			try:
				response.delete_cookie('filter_car_date', None, -1000)
			except:
				pass

		if car_for_loan is not None:
			try:
				response.set_cookie('filter_car_for_loan', car_for_loan)
			except:
				pass
		else:
			try:
				response.delete_cookie('filter_car_for_loan', None, -1000)
			except:
				pass
		return response
	else:
		return HttpResponseRedirect('/car/list/')


def car_filter_reset(request):
	if request.POST:
		response = HttpResponseRedirect('/car/list/')

		for cookie in request.COOKIES:
			if str('filter') in cookie:
				response.delete_cookie(cookie)
		return response
	else:
		return HttpResponseRedirect('/car/list/')


def car_save(request):
	args['title'] = u"Загрузить новые автомобили"
	try:
		args['json'] = j_son = json.loads(request.POST.get("car_json"))
	except:
		args['json'] = j_son = None
	if j_son is not None:
		companies = j_son['Cars']['Companies']
		cars = j_son['Cars']['Car']
		for co_group in companies:

			### Saving CompanyGROUP ###
			company_group_save_form = CarCompanyGroupForm(request.POST)
			try:
				company_group = CarCompanyGroup.objects.get(id=co_group['CompanyGroupId'])
			except:
				company_group = None

			if company_group is not None:
				pass
			else:
				new_company_group = company_group_save_form.save(commit=False)
				new_company_group.id = co_group['CompanyGroupId']
				new_company_group.car_company_group_name = co_group['CompanyGroupName']
				new_company_group.save()
			### End CompanyGROUP Saving ###

			### Saving COMPANY ###
			for co_company in co_group['GroupCompanies']:

				company_save_form = CarCompanyForm(request.POST)
				try:
					company = CarCompany.objects.get(id=co_company['ComapnyINN'])
				except:
					company = None

				if company is not None:
					pass
				else:
					try:
						company_group = CarCompanyGroup.objects.get(id=co_group['CompanyGroupId'])
					except:
						company_group = None
					if company_group is not None:
						new_company = company_save_form.save(commit=False)
						new_company.id = co_company['ComapnyINN']
						new_company.car_company_inn = co_company['ComapnyINN']
						new_company.car_company_name = co_company['CompanyName']
						new_company.car_company_car_group = company_group
						new_company.save()
					else:
						pass
					### End COMPANY Saving ###

		for car in cars:

			### Saving CAR ###
			car_save_form = CarForm(request.POST)
			try:
				current_car = Car.objects.get(car_vin=car['VIN'])
			except:
				current_car = None

			if current_car is not None:
				pass
			else:
				new_car = car_save_form.save(commit=False)
				new_car.id = car['Id']
				new_car.car_for_loan = car['ForLoan']
				new_car.car_car_company_group_id = car['CompanyGroupId']
				new_car.car_car_company_id = car['CompanyINN']
				new_car.car_vin = car['VIN']
				new_car.car_category = car['Category']
				if car['Kilometrage'] <= 10000:
					new_car.car_type = 1
				else:
					new_car.car_type = 0
				new_car.car_accident = car['Accident']
				new_car.car_make = car['Make']
				new_car.car_model = car['Model']
				new_car.car_year = car['Year']
				new_car.car_km = car['Kilometrage']
				new_car.car_body = car['BodyType']
				new_car.car_transmission = car['Transmission']
				new_car.car_fuel = car['FuelType']
				new_car.car_door = car['Doors']
				new_car.car_color = car['Color']
				new_car.car_engine_size = car['EngineSize']
				new_car.car_price = car['Price']
				new_car.car_vnumber = car['Gosnomer']
				new_car.save()
			### End CAR Saving ###

			### Saving CAR IMAGE ###
			for car_image in car['Images']['CarImage']:

				company_image_save_form = CarImageForm(request.POST)
				try:
					current_car = Car.objects.get(car_vin=car['VIN'])
				except:
					current_car = None

				if current_car is not None:
					try:
						current_car_image = CarImage.objects.get(car_image_url=car_image['-url'])
					except:
						current_car_image = None
					if current_car_image is None:
						new_car_image = company_image_save_form.save(commit=False)
						new_car_image.car_image_url = car_image['-url']
						new_car_image.car_image_car = current_car
						new_car_image.save()
					else:
						pass
				else:
					pass
				### End CAR IMAGE Saving ###

		return render(request, 'car_add.html', args)
	else:
		return render(request, 'car_add.html', args)


def car_export_xls(request):
	if request.POST:
		response = HttpResponse(content_type='application/ms-excel')
		filename = u"ÐÐ²ÑÐ¾Ð¼Ð¾Ð±Ð¸Ð»Ð¸.xls"
		response['Content-Disposition'] = 'attachment;' + 'filename=' + filename

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Автомобили')

		# Sheet header, first row
		row_num = 0

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = [
			'Компания',
			'ИНН компании',
			'VIN код',
			'Марка',
			'Модель',
			'Год',
			'Цена',
			'Госномер',
			'Пробег',
			'Для продажи'
		]

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style)

		# Sheet body, remaining rows
		font_style = xlwt.XFStyle()

		selected_cars = request.POST.getlist('car_id')
		if selected_cars is not None:
			rows = Car.objects.filter(
				id__in=selected_cars
			).values_list(
				'car_car_company__car_company_name',
				'car_car_company__car_company_inn',
				'car_vin',
				'car_make',
				'car_model',
				'car_year',
				'car_price',
				'car_vnumber',
				'car_km',
				'car_for_loan',
			)
		else:
			rows = Car.objects.all().values_list(
				'car_car_company__car_company_name',
				'car_car_company__car_company_inn',
				'car_vin',
				'car_make',
				'car_model',
				'car_year',
				'car_price',
				'car_vnumber',
				'car_km',
				'car_for_loan',
			)
		for row in rows:
			row_num += 1
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)

		wb.save(response)
		return response
	else:
		return HttpResponseRedirect('/')
