from builtins import Exception

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.db import transaction

from .models import User
from .serializer import UserSerializer


# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )

    @transaction.atomic
    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def sing_up(self, request):
        data = request.data

        try:
            if User.objects.filter(username=data['email']).exists():
                return Response({'mesage':'email is already in use'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                user = User.objects.create(
                    full_name=data['full_name'],
                    email=data['email'],
                    username=data['email'],
                )

                user.set_password(data['password'])
                user.save()

            token = Token.objects.get_or_create(user=user)
            user_serializer = self.serializer_class(user)

            return Response({'mesage': 'User created', 'user': user_serializer.data,
                             'token': token[0].__str__()}, status=status.HTTP_200_OK)

        except Exception as error:
            print(error)
            return Response({'error': error.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny, ))
    def sing_in(self, request):
        data = request.data

        user = authenticate(username=data['email'], password=data['password'])

        if user is None:
            return Response({'mesage': 'No User Found'}, status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user=user)
        user_serializer = self.serializer_class(user)

        return Response({'mesage': 'User Found', 'user': user_serializer.data,
                         'token': token.__str__()}, status=status.HTTP_200_OK)
