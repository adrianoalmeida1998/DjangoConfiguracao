from django.urls import path
from notas.views import index, dashboard


urlpatterns = [
    path('', index, name='index'),          # Página inicial
    path('dashboard/', dashboard, name='dash'),
]