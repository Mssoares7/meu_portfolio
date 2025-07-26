from django.db import models
from cloudinary.models import CloudinaryField

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    imagem = CloudinaryField('imagem', blank=True, null=True)  # alterado
    link_demo = models.URLField(blank=True)
    link_codigo = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    imagem = CloudinaryField('imagem', blank=True, null=True)  # alterado
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
