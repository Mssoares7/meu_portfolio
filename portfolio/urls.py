from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('curriculo-en/', views.curriculo_en, name='curriculo_en'),
    path('projetos/<int:pk>/', views.projeto_detail, name='projeto_detail'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path('rodar-migracoes/', views.rodar_migracoes, name='rodar_migracoes'),
    path('criar-admin/', views.cria_superusuario, name='criar_superusuario'),
]