from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.contrib.auth import views as auth_views

from grupo5.views import (   
    login,
    registro_user,
    index,
    perfil,
    garage,
    venta_auto,
    contacto
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='index/', permanent=False)),  
    path('index/', views.index, name='index'),
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('perfil.html', perfil, name='perfil'),
    path('registro_user/', registro_user, name='registro_user'),
    path('garage/', garage, name='garage'),
    path('venta_auto/', venta_auto, name='venta_auto'),
    path('contacto/', contacto, name='contacto'),   
    # login y logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]

