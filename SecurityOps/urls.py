from django.urls import path
from . import views

urlpatterns = [
    # 🔐 LOGIN COMO PÁGINA INICIAL (OBRIGATÓRIO PARA SEU TRABALHO)
    path('', views.login_view, name='login'),

    # 🏠 HOME (após login)
    path('home/', views.home, name='home'),

    # 🔓 LOGOUT
    path('logout/', views.logout_view, name='logout'),

    # 🔥 INCIDENTES (CRUD)
    path('incidente/', views.incidente, name='incidente'),
    path('incidente/editar/<int:id>/', views.editar_incidente, name='editar_incidente'),
    path('incidente/excluir/<int:id>/', views.excluir_incidente, name='excluir_incidente'),

    # 📚 CURSOS
    path('cursos/', views.cursos, name='cursos'),
]