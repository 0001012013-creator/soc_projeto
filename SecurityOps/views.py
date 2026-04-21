from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import IncidenteForm
from .models import Incidente


# =========================
# LOGIN
# =========================
def login_view(request):
    erro = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            erro = "Usuário ou senha inválidos"

    return render(request, 'login.html', {'erro': erro})


def logout_view(request):
    logout(request)
    return redirect('login')


# =========================
# HOME
# =========================
@login_required
def home(request):
    return render(request, 'home.html')


# =========================
# INCIDENTES - LISTAR + CRIAR
# =========================
@login_required
def incidente(request):
    incidentes = Incidente.objects.all()

    form = IncidenteForm()

    if request.method == 'POST':
        form = IncidenteForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('incidente')

    return render(request, 'incidente.html', {
        'form': form,
        'incidentes': incidentes
    })


# =========================
# EDITAR
# =========================
@login_required
def editar_incidente(request, id):
    incidente_obj = get_object_or_404(Incidente, id=id)

    if request.method == 'POST':
        form = IncidenteForm(request.POST, request.FILES, instance=incidente_obj)

        if form.is_valid():
            form.save()
            return redirect('incidente')
    else:
        form = IncidenteForm(instance=incidente_obj)

    return render(request, 'incidente.html', {
        'form': form,
        'incidentes': Incidente.objects.all()
    })


# =========================
# EXCLUIR
# =========================
@login_required
def excluir_incidente(request, id):
    incidente_obj = get_object_or_404(Incidente, id=id)
    incidente_obj.delete()
    return redirect('incidente')


# =========================
# CURSOS
# =========================
@login_required
def cursos(request):
    return render(request, 'cursos.html')