from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import include
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import TodoItem
from .serializers import RegisterSerializer,loginSerializer,TodoItemSerializer

# Create your views here.

# @method_decorator(csrf_exempt, name='dispatch')
class RegisterUserView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    # authentication_classes = []
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({ 'id': user.id,
        'username': user.username,
        'email': user.email,
        'token':access_token}, status = status.HTTP_201_CREATED)
    


# @method_decorator(csrf_exempt, name='dispatch')
class LoginView(ListCreateAPIView):
    serializer_class = loginSerializer
    permission_classes =[AllowAny]
    authentication_classes = []



    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = serializer.validated_data['user']
        except KeyError:
                return Response({'success': false, 'error':'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({ 'id': user.id,
        'username': user.username,
        'email': user.email,
        'token':access_token}, status = status.HTTP_200_OK)



class TodoItemListCreate(ListCreateAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    page_size = 10

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
        

class ListTodoItems(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
   
    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user).order_by('-created_at')
    



