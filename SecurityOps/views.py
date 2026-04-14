from django.shortcuts import render, redirect
from .forms import IncidenteForm

def home(request):
    return render(request, 'home.html')

def incidente(request):
    if request.method == 'POST':
        form = IncidenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncidenteForm()

    return render(request, 'incidente.html', {'form': form})

def cursos(request):
    return render(request, 'cursos.html')