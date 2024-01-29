"""online_clinic_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from frist_page.views import *
from signin.views import *
from signup.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup/', signup, name='signup'),
    path('signup/signup_success', signup_success, name='signup_success'),
    path('signin/', signin, name='signin'),
    path('secretary_page/', secretary_page, name='secretary_page'),
    path('patient_page/', patient_page, name='patient_page'),
    path('reserving_appointment/', reserving_appointment, name='reserving_appointment'),
    path('payment_page/', payment_page, name='payment_page'),
    path('pay/', pay, name='pay'),
    path('payment_success/', payment_success, name='payment_success'),
    path('previous_appointments/', previous_appointments, name='previous_appointments'),
    path('current_appointment/', current_appointment, name='current_appointment'),
    path('increase_capacity_info/', increase_capacity_info, name='increase_capacity_info'),
    path('increase_capacity/', increase_capacity, name='increase_capacity')]