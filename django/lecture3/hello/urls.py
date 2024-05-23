from django.urls import path

from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("hello-dublin", views.helloDublin, name="hello-dublin"),
     path("<str:city>", views.greatCity, name="city"),
     path("<str:name>", views.sayHello, name="say-hello")
]