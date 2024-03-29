"""
URL configuration for MonProjectEstore project.

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
from django.urls import include
from shop.views import index ,detail, checkout, confirmation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls' , namespace='account')),
    path('supplier/', include('supplier.urls')),
    path('', index, name='home'),  
    path('shop/', include('shop.urls', namespace='shop')),
    path('', index, name='home'),
    path('<int:id>/', detail, name="detail"),
    path('checkout/', checkout, name="checkout"),
    path('confirmation/', confirmation, name="confirmation"),
   
]
