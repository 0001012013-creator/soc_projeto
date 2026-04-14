from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('incidente/', views.incidente, name='incidente'),
    path('cursos/', views.cursos, name='cursos'),
]