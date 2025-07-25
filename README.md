# 💼 Meu Portfólio Profissional

Este é meu portfólio online desenvolvido com **Django**, onde apresento meus projetos práticos, estudos técnicos e publicações com base nos livros que tenho estudado.

## 🛠️ Tecnologias utilizadas

- Django 5.2
- Python 3.11
- HTML + CSS + JavaScript (puro)
- SQLite (modo desenvolvimento)
- PostgreSQL (opcional para produção)
- Render (para deploy)
- Git e GitHub

## ✨ Funcionalidades

- Página de **projetos** com filtro por tecnologias
- Página de **currículo** em português e inglês (com modo impressão)
- Página de **publicações técnicas** com textos e imagens
- Design responsivo e pronto para deploy

## 📂 Estrutura de pastas

```bash
meu_portfolio/
├── portfolio/           # App principal
│   ├── models.py        # Modelos: Projeto, Publicacao, Tecnologia
│   ├── views.py         # Lógica das views
│   ├── templates/       # Templates HTML
│   └── static/          # CSS, JS, imagens
├── config/              # Configurações Django
│   └── settings.py      # Configurações principais
├── media/               # Uploads de imagens dos projetos/publicações
├── staticfiles/         # Pasta gerada no collectstatic (produção)
├── db.sqlite3           # Banco de dados local
├── requirements.txt     # Dependências
├── Procfile             # Instrução de start para o Render
├── .render.yaml         # Configuração para deploy automático
├── .env                 # Variáveis de ambiente (não versionado)
└── README.md            # Você está aqui
🚀 Deploy
Projeto preparado para deploy gratuito no Render, com:

Procfile e .render.yaml

Suporte a collectstatic

Variáveis de ambiente via .env

Modo produção com DEBUG=False

🧑‍💻 Autor
Matheus da Silva Soares
https://www.linkedin.com/in/matheus-da-silva-soares/ | https://github.com/Mssoares7