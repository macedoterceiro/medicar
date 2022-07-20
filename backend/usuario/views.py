# from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from usuario.serializers import UserRegistrationSerializer

class UserRegistrationAPIView(APIView):
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            data['username'] = new_user.username
            data['email'] = new_user.email
        else:
            data = serializer.errors
        
        return Response(data=data)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'name': f'{user.first_name} {user.last_name}' ,
        })
