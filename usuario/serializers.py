from rest_framework import exceptions
from rest_framework import serializers

from usuario.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name', 'last_name','username', 'email', 'password']
        extra_kwargs ={
            'password':{'write_only': 'password'}
        }
    
    def validate(self,data):
        def validate_email(data):
            try:
                user = User.objects.get(email=data['email'])
                raise serializers.ValidationError({'email':'Email já cadastrado!'})
            except User.DoesNotExist:
                pass
        def validate_name(data):
            if len(data['first_name']) == 0:
                raise serializers.ValidationError({'nome':'O campo não pode estar em branco!'})
            elif len(data['last_name']) == 0:
                raise serializers.ValidationError({'sobrenome':'O campo não pode estar em branco!'})
        
        validate_name(data)
        validate_email(data)
        return data

    def save(self,):
        new_user = User(username=self.validated_data['username'], 
                        email=self.validated_data['email'],
                        first_name=self.validated_data['first_name'],
                        last_name=self.validated_data['last_name'],
                        )
        new_user.set_password(self.validated_data['password'])
        new_user.save()
        return new_user