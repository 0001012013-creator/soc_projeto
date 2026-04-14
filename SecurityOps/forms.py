from django import forms
from .models import Incidente

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ['nome_completo', 'matricula', 'titulo', 'descricao', 'imagem']