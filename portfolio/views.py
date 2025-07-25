from django.shortcuts import render, get_object_or_404
from .models import Projeto, Tecnologia, Publicacao
from django.core.management import call_command
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def home(request):
    projetos = Projeto.objects.all()
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/home.html', {
        'projetos': projetos,
        'tecnologias': tecnologias
    })

def curriculo(request):
    return render(request, 'portfolio/curriculo.html')

def curriculo_en(request):
    return render(request, 'portfolio/curriculo_en.html')

def projeto_detail(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'portfolio/projeto_detail.html', {'projeto': projeto})

def publicacoes(request):
    publicacoes = Publicacao.objects.order_by('-data_publicacao')
    return render(request, 'portfolio/publicacoes.html', {'publicacoes': publicacoes})

def rodar_migracoes(request):
    call_command('migrate')
    return HttpResponse("Migrações aplicadas com sucesso.")

def cria_superusuario(request):
    from django.contrib.auth.models import User
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        return HttpResponse("Superusuário criado com sucesso.")
    else:
        return HttpResponse("Superusuário já existe.")

def redefinir_senha_admin(request):
    try:
        user = User.objects.get(username="admin")
        user.set_password("admin321")
        user.save()
        return HttpResponse("Senha redefinida com sucesso para 'admin321'.")
    except User.DoesNotExist:
        return HttpResponse("Usuário admin não encontrado.")

def redefinir_senha_admin(request):
    User = get_user_model()
    username = "admin"
    password = "admin321"

    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()

    if created:
        return HttpResponse("Superusuário 'admin' criado com sucesso.")
    else:
        return HttpResponse("Senha redefinida para o usuário 'admin'.")