from django.urls import path
from . import views  

urlpatterns = [
   
    path('suppliers/', views.suppliers, name='add_supplier'),  
    path('supplier_show/', views.show, name='supplier_show'),  
]

    



