from django.shortcuts import render,HttpResponse

# Create your views here.

def index(reqyest):
    return HttpResponse('<h1>Página de inicio<h1>')
    
