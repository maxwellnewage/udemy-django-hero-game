from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from character.models import Player
from .serializers import PlayerSerializer
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            response_data = {
                "success": True,
                "message": "Jugador creado exitosamente.",
                "player": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                "success": False,
                "message": "Error al crear el jugador.",
                "player": serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Se debe indicar usuario y contraseña'}, status=status.HTTP_204_NO_CONTENT)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response({'error': 'El usuario o la contraseña son incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)
