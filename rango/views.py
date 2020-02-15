from django.shortcuts import render

from django.http import HttpResponse
def index(request):
   return HttpResponse("Rango says hey there partner!"+'<a href="/rango/about/">http://127.0.0.1:8000/rango/</a>')
   
def about(request):
   return HttpResponse( 'Rango says here is the about page.'+'<a href="/rango/">http://127.0.0.1:8000/</a>')