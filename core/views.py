from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
<h1>Mi web personal</h1>
<ul> 
    <li><a href='/'> Home </a></li>
    <li><a href='/fotos/'> Fotos </a></li>
    <li><a href='/email/'> Email </a></li>
    <li><a href='/contacto/'> Contacto </a></li>
</ul>
"""



def home(request):
    return HttpResponse (html_base + "<h2>Hola amigos del curso. Gracias por atender.</h2>")  

def fotos(request):
    return HttpResponse (html_base + "<h3>Aquí vemos nuestras fotos.</h3>")    

def email(request):
    return HttpResponse (html_base +"<h2>Aqui dejad vuestro email.</h2>")    

def contacto(request):
    return HttpResponse (html_base + "<h2>Si tenéis dudas, pues preguntar joder.</h2>")     