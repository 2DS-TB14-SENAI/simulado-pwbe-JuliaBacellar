from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

@api_view(['POST'])
def registro(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    telefone = request.data.get('telefone')


    if User.objets.filter(username=username).exists():
        return Response({'error': 'usuario ja existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username,password=password, telefone=telefone)
    return Response({'message': 'usuario criado com sucesso'}, status=status.HTTP_201_CREATED)




