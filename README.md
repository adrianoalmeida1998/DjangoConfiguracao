Configuração inicial
1 - Crie o ambiente virtual.
# Windows
python -m venv venv
venv\\Scripts\\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate

-------------------------------------

2 - Instale as dependências

pip install django

---------------------------------------
Essas dependências não foi utilizada

pip install pillow
pip install django-crispy-forms
pip install crispy-bootstrap5 
-----------------------------------------

# Ou se tiver requirements.txt
pip freeze -r requirements.txt

# Grava um requirements
pip freeze > requirements.txt

-----------------------------------------
Para criar SuperUsuário.

python manage.py migrate
python manage.py createsuperuser



🚀 Projeto Django - Sistema de Notas






📌 Sobre o Projeto

Este projeto foi desenvolvido utilizando o framework Django com o objetivo de praticar:

Estrutura de projetos Django

Configuração de rotas (urls)

Renderização de templates

Organização de aplicações

Versionamento com Git e GitHub

O sistema possui uma página inicial e um dashboard, com estrutura preparada para expansão futura.

🛠️ Tecnologias Utilizadas

Python 3.x

Django

HTML5

CSS3

SQLite (padrão do Django)

Git & GitHub

⚙️ Configuração do Ambiente
🔹 1. Criar Ambiente Virtual
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python -m venv venv
source venv/bin/activate
🔹 2. Instalar Dependências
pip install django

Dependências opcionais testadas (não utilizadas atualmente):

pip install pillow
pip install django-crispy-forms
pip install crispy-bootstrap5
🔹 3. Gerar ou Instalar Requirements
Gerar arquivo:
pip freeze > requirements.txt
Instalar dependências:
pip install -r requirements.txt
🗄️ Banco de Dados

Aplicar migrações:

python manage.py migrate
👤 Criar SuperUsuário
python manage.py createsuperuser

Acesse o painel administrativo em:

http://127.0.0.1:8000/admin/
▶️ Executar o Projeto
python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/
📂 Estrutura do Projeto
ProjetoDjangoCurso/
│
├── notas/               # Aplicação principal
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── setup/               # Configurações do projeto
│   ├── settings.py
│   └── urls.py
│
├── templates/           # Arquivos HTML
│   ├── index.html
│   └── dashboard.html
│
├── manage.py
└── requirements.txt
🌐 Rotas do Sistema
URL	Página
/	Página Inicial
/dashboard/	Dashboard
/admin/	Painel Administrativo
📌 Funcionalidades Atuais

✔️ Página inicial
✔️ Dashboard
✔️ Navegação entre páginas
✔️ Painel administrativo Django

🚧 Melhorias Futuras

 Sistema de cadastro de notas

 Autenticação de usuários

 Estilização com Bootstrap

 Deploy em servidor (Render ou Railway)

 Implementação de CRUD completo


 📈 Objetivo do Projeto

Este projeto faz parte do meu processo de aprendizado em desenvolvimento backend com Django, com foco em:

Organização de código

Boas práticas

Estrutura profissional de projeto

Controle de versão com Git

👨‍💻 Autor

Desenvolvido por Adriano Almeida
GitHub: https://github.com/adrianoalmeida1998