from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import TodoItem


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self ,validated_data):
        password = validated_data.pop('password')  # remove password from validated_data
        user = User(**validated_data)              # create user instance without password
        user.set_password(password)                # set hashed password
        user.save()                        # save user to database
        return user             
    
    def validate_password(self,value):
        if len(value)< 6:
            raise serializers.ValidationError('Password must contain at least 6 characters.')
        return value           # return the created user instance



class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)   
            if not user:
                raise serializers.ValidationError('Invalid credentials')
        else: 
            raise serializers.ValidationError('Both username and password are required')
        
        data['user'] = user
        return data
    

class TodoItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at','user']
        read_only_fields = ['id', 'created_at', 'updated_at','user']
  
   