"""
URL configuration for MSYS22FP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('view_Employees', views.view_Employees, name='view_Employees'),
    path('create_employee', views.create_Employee, name='create_Employee'),
    path('update_employee/<int:pk>/', views.update_Employee, name='update_Employee'),
    path('view_payslips', views.view_Payslips, name='view_Payslips'),
    path('delete_employee/<int:pk>/', views.delete_Employee, name='delete_Employee'),
    path('update_OT/<int:pk>', views.update_OT, name='update_OT'),
    path('view_receipt/<int:pk>', views.view_Receipt, name='view_receipt'),
]

urlpatterns += staticfiles_urlpatterns()