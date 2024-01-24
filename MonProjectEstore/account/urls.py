from django.urls import path
from django.contrib import admin
from django.urls.conf import include
from account import views

app_name = "account"
urlpatterns = [
    path('admin', admin.site.urls),
    path('loginPage',views.LoginPage,name='login'),
    path('home',views.HomePage,name='home'),
    path('SignupPage',views.SignupPage,name='signup'),
    path('logout',views.LogoutPage,name='logout'),
   

]    
