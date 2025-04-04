from django.urls import path
from django.urls import registro 

urlpatterns = [
    path('auth/registro/', registro, name='registro'),
]
