from django.urls import path
from django.contrib import admin
from django.urls.conf import include
from account import views
from shop.views import index ,detail, checkout, confirmation


app_name = "account"
urlpatterns = [
    path('admin', admin.site.urls),
    path('loginPage',views.LoginPage,name='login'),
    path('home',views.HomePage,name='home'),
    path('SignupPage',views.SignupPage,name='signup'),
    path('logout',views.LogoutPage,name='logout'),
    path('fournisseur',views.FournisseurPage,name='fournisseur'),
    path('', index, name='home'),  
    path('shop/', include('shop.urls', namespace='shop')),
    path('', index, name='home'),
    path('<int:id>/', detail, name="detail"),
    path('checkout/', checkout, name="checkout"),
    path('confirmation/', confirmation, name="confirmation"),
   

]    
