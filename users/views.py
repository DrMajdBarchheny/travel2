from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer , UserSerializerWithToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsersProfile(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['name'] ,
            username = data['email'] , 
            email = data['email'] , 
            password = make_password(data['password'])
            )
        serializer =UserSerializerWithToken(user , many=False)
        return Response(serializer.data)
    except:
        message ={'detail':'There is another account with the same email'}
        return Response(message , status=status.HTTP_400_BAD_REQUEST)
