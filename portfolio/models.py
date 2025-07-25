from django.db import models

# Create your models here.

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    link_demo = models.URLField(blank=True)
    link_codigo = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='publicacoes/', blank=True, null=True)
    publicado = models.BooleanField(default=True)


    def __str__(self):
        return self.titulo
