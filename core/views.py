from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render (request, "core/home.html")  

def fotos(request):
    return render (request, "core/fotos.html")      

def email(request):
    return render (request, "core/email.html")    

def contacto(request):
    return render (request, "core/contacto.html")      

