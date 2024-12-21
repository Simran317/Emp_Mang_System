"""EmpRecoMg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.index, name ='index'),
    path('registration/', views.registration, name = "registration"),
    path('emp_login/', views.emp_login, name ="emp_login"),
    path('emp_home/', views.emp_home, name = 'emp_home'),
    path('profile/', views.profile, name = "profile"),
    path('logout/', views.Logout, name ="logout"),
    path('admin_login/', views.admin_login, name = "admin_login"),
    path('my_exp/', views.my_exp, name = "my_exp"),
    path('edit_exp/', views.edit_exp, name = "edit_exp"),
    path('my_education/',views.my_education, name = "my_education"),
    path('edit_education/', views.edit_education, name = "edit_education"),
    path('achievement/', views.achievement, name = "achievement"),

    path('Paper_publication/', views.Paper_publication, name = "Paper_publication"),
    path('journals/', views.journals, name = "journals"),
    path('change_password/', views.change_password, name = "change_password"),
    path('admin_home/', views.admin_home, name = "admin_home"),
    path('admin_change_password/', views.admin_change_password, name = "admin_change_password"),
    path('all_employee/', views.all_employee, name = "all_employee" ),

]
