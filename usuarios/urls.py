from django.urls import path
from . import views


urlpatterns = [
    path('auth/registro/', views.registro, name='registro'),
    
]
