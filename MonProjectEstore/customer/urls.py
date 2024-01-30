from django.urls import path
from customer import views


urlpatterns = [
    path('customer',views.customer, name='add'),
    path('show',views.show, name='customer'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
]