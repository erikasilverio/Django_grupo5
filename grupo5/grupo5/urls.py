from django.contrib import admin
from django.urls import path,include
from django.conf import settings


from django.contrib.auth import views as auth_views


from . import views
from grupo5 import views


from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(('libreria.urls', 'lib'), namespace='lib')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login' ),
 
    path('', RedirectView.as_view(url='index/', permanent=False)),
    path('index/', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('registro_user/', views.registro_user, name='registro_user'),
    path('garage/', views.garage, name='garage'),
    path('venta_auto/', views.venta_auto, name='venta_auto'),
    path('contacto/', views.contacto, name='contacto'),
]

