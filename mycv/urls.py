from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name='mycv_home'),
	path('hire_me/', views.hire_me, name='hire_form')	
]
