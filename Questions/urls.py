from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [

	url(r'^list$',views.list,name='list'),


	]