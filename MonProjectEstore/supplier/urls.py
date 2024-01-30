from django.urls import path
from supplier import views

urlpatterns = [
    path('suplpliers',views.suppliers,),
    path('supplier_show',views.show, name='suppliers'),
    
]