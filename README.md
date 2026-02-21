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
