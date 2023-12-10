from django.shortcuts import render, redirect

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'libreria/index.html'
    login_url = 'pages:login'




def perfil(request):
    return render(request,'perfil.html')

def registro_user(request):
    return render(request,'registro_user.html')

def garage(request):
    return render(request,'garage.html')

def venta_auto(request):
    return render(request,'venta_auto.html')

def contacto(request):
    return render(request,'contacto.html')