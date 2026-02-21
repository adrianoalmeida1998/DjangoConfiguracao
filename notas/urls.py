from django.urls import path
from notas.views import index

urlpatterns = [
  path('', index,name='index'),
]