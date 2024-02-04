"""AssetManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asset_tracker import views

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    path('add_company/', views.add_company, name='add_company'),
    path('company/<int:company_id>/employees/', views.employee_list, name='employee_list'),
    path('company/<int:company_id>/add_employee/', views.add_employee, name='add_employee'),
    path('devices/', views.device_list, name='device_list'),
    path('add_device/', views.add_device, name='add_device'),
    path('device/<int:device_id>/', views.device_detail, name='device_detail'),
    path('device/<int:device_id>/checkout/', views.checkout_device, name='checkout_device'),
    path('device/<int:device_id>/return/', views.return_device, name='return_device'),
]
