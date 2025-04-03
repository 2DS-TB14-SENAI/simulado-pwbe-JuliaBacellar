from django.urls import path 
from .views import listar_livros

urlpatterns = [
    path('livros/', listar_livros, name='listar_livros'),

]