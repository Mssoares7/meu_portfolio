from django.contrib import admin
from .models import Projeto, Tecnologia, Publicacao

# Register your models here.

admin.site.register(Projeto)
admin.site.register(Tecnologia)
@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'texto')