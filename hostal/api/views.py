from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import HuespedSerializer, ClienteSerializer
from website.models import Huesped, Cliente

@api_view(['POST'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        content = {'Usuario no existe':'User does not exist'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    if not check_password(password,user.password):
        content = {'Password invalido':'Password incorrect'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response(token.key)

class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()
    print("Logout")
    def get(self,request,format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_ok)

class HuespedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticated]