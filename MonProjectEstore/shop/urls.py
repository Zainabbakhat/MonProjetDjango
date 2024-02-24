from django.urls import path, include
from shop.views import index, detail, checkout, confirmation 
app_name = 'shop'

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>', detail, name="detail"),
    path('checkout/', checkout, name="checkout"),
    path('confirmation/', confirmation, name="confirmation" ),
  
]




    