from django.shortcuts import render,HttpResponse

#MODELS
from .models import Project
# Create your views here.

def profile(request):

    projects = Project.objects.all()
    
    return HttpResponse(projects)
    
