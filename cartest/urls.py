"""cartest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from car import views as car_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', car_views.car_list),
    url(r'^car/list/$', car_views.car_list),
    url(r'^car/list/(\d+)/$', car_views.car_list),
    url(r'^car/profile/(?P<car_id>[\w\-]+)/$', car_views.car_profile),

	url(r'^car/change-show-count/$', car_views.car_change_show_count),
	url(r'^car/change-order-by/$', car_views.car_change_order_by),
	url(r'^car/filter-set/$', car_views.car_filter_set),
	url(r'^car/filter-reset/$', car_views.car_filter_reset),
	url(r'^car/export-xls/$', car_views.car_export_xls),

    url(r'^car/car-add/$', car_views.car_add),
    url(r'^car/car-save/$', car_views.car_save),
]
