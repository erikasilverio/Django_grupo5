from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class Home(LoginRequiredMixin, View):
    template_name = 'libreria/index.html'
    login_url = 'login'

    def get(self, request):
        return render(request, self.template_name)



def registro_user(request):
    return render(request, 'registro_user.html')

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def garage(request):
    return render(request, 'garage.html')

def venta_auto(request):
    return render(request, 'venta_auto.html')

def contacto(request):
    return render(request, 'contacto.html')



#logout =============

def custom_logout(request):
    logout(request)
    return redirect('/index')

#logout =============


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index.html') 

    return render(request, 'login.html')
