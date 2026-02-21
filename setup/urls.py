from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notas.urls')),  # ← aqui está a mudança
]








#setup.urls.py > notas.urls vai chamar ---> url ------> views.py > index() > HttpResponse