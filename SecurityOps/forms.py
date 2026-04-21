from django import forms
from .models import Incidente

class IncidenteForm(forms.ModelForm):
    imagem = forms.ImageField(
        required=False,
        widget=forms.FileInput  # 🔥 remove "Limpar" e "Modificar"
    )

    class Meta:
        model = Incidente
        fields = ['nome_completo', 'matricula', 'titulo', 'descricao', 'imagem']