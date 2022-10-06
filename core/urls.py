from django.urls import path

#VIEWS

from . import views


#CINFIGURANDO URLS

urlpatterns = [
    path('', views.index, name = 'home' ),
]