from django.db import models

class Incidente(models.Model):
    nome_completo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    imagem = models.ImageField(
        upload_to='incidentes/',
        null=True,
        blank=True
    )

    # 🔥 CORREÇÃO
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo