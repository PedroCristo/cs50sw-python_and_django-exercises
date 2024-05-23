from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Create views to render html template
def index(request):
    return render(request, "hello/index.html")

def greatCity(request, city):
    return render(request, "hello/city.html", {
        "city": city.capitalize()
    })   

def helloDublin(request):
    return HttpResponse("Hello Dublin")

# Create viws using str
def sayHello(request, name):
    return HttpResponse (f"Hello, {name.capitalize()}")   

      
