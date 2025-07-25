from django.urls import path
from . import views
from django.urls import path
from .views import cria_superusuario

urlpatterns = [
    path('', views.home, name='home'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('curriculo-en/', views.curriculo_en, name='curriculo_en'),
    path('projetos/<int:pk>/', views.projeto_detail, name='projeto_detail'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path("criar-admin-secret-2782/", cria_superusuario),  # use um nome bem aleatório aqui!
]
