from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

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