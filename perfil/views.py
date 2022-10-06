from django.shortcuts import render,HttpResponse

# Create your views here.

def profile(request):
    return HttpResponse('<h2> PAGINA DE PERFIL <h2>')
    
