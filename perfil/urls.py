from django.urls import path

#VIEWS

from . import views


#CINFIGURANDO URLS

urlpatterns = [
    path('', views.profile, name = 'profile' ),
]