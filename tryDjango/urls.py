"""tryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from pages.views import love,new
from products.views import (
            products_detail,
            products_create,
            dynamic_lookup_view,
            products_createX,
            product_delete_view,
            product_edit_view,
            home_view,
            dynamic_detail
            )
#from products.views import Home


urlpatterns = [
    path('',home_view,name='home'),
    path('love/',love),
    path('create/',products_create,name='add-product'),
    path('createX/',products_createX),
    path('love/new/',new),
    path('admin/', admin.site.urls),
    path('product/',products_detail),
    path('detail/',dynamic_detail,name='dynamic-detail'),
    path('detail/<int:my_id>/',dynamic_lookup_view,name='dynamic-lookup'),
    path('detail/<int:my_id>/edit/',product_edit_view,name='product-edit'),
    #re_path(r'^detail/(?P<my_id>\w+)/edit/',product_edit_view , name='product-edit'),
    path('detail/<int:my_id>/delete/',product_delete_view,name='product-delete'),
    
    #path('noob/', Home.as_view(), name='home'),
]
