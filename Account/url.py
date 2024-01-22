from django.urls import path
from . import views

app_name = "MonProjet"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.loginpage, name='loginpage'),
    path('signup/', views.signuppage, name='signuppage'),
    path('logout/', views.logoutpage, name='logoutpage'),
]

