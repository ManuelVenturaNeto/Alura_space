from django.shortcuts import render # type: ignore

def login(request):
    return render(request, "usuarios/login.html")

def cadastro(request):
    return render(request, "usuarios/cadastro.html")
