"""
URL configuration for projectfakeproduct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from administator.views import AdminDashboard, ForgetPassword, Login, MainPage, ManufactureDashboard, ProductAdd, ProductApprove, ProductEdit, ProductFeedback, ProductManage, ProductUpdate, Register, ViewUser
urlpatterns = [

# ///////////////////////////////// admin /////////////////////////////
    path('AdminDashboard',AdminDashboard.as_view(),name='AdminDashboard'),
    path('ProductApprove',ProductApprove.as_view(),name='ProductApprove'),
    path('ProductFeedback',ProductFeedback.as_view(),name='ProductFeedback'),
    path('ForgetPassword',ForgetPassword.as_view(),name='ForgetPassword'),
    path('ViewUser',ViewUser.as_view(),name='ViewUser'),

# ////////////////////////////////// manufacture     /////////////////////////
    path('ProductAdd',ProductAdd.as_view(),name='ProductAdd'),
    path('ProductEdit',ProductEdit.as_view(),name='ProductEdit'),
    path('ProductManage',ProductManage.as_view(),name='ProductManage'),
    path('ManufactureDashboard',ManufactureDashboard.as_view(),name='ManufactureDashboard'),
    path('Register',Register.as_view(),name='Register'),
    path('ProductUpdate',ProductUpdate.as_view(),name='ProductUpdate'),


    path('Login',Login.as_view(),name='Login'),
    path('MainPage',MainPage.as_view(),name='MainPage'),
]
