"""
URL configuration for E_Commerce project.

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
from django.urls import path,include

from apps.cart.views import cart_detail
from apps.e_com.views import home,contact,about
from apps.store.views import product_detail,category_detail

from apps.store.api import api_add_to_cart,api_remove_from_cart

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('',home, name="home"),
    path('cart/',cart_detail, name="cart"),
    path('contact/',contact, name="contact"),
    path('about/',about, name="about"),

    #api
    path('api/add_to_cart/',api_add_to_cart, name="api_add_to_cart"),
    path('api/remove_from_cart/',api_remove_from_cart, name="api_remove_from_cart"),
    #store
    path('<slug:category_slug>/<slug:slug>/', product_detail, name="product_detail"),
    path('<slug:slug>/', category_detail, name="category_detail"),
    
]
