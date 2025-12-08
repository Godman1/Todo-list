from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TodoItem
from .serializers import RegisterSerializer,loginSerializer,TodoItemSerializer

# Create your views here.
@api_view(['GET','POST'])
def register_user(request):
    if request.method == 'GET':
        # queryset = get_user_model().objects.all()
        # serializer = RegisterSerializer(queryset, many=True)
        return Response('User Registration Endpoint')
    elif request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        # return Response(serializer.data )
        return Response({ 'id': user.id,
        'username': user.username,
        'email': user.email,
        'token':access_token}, status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])    
def login_user(request):
    if request.method == 'GET':
        return Response('User Login Endpoint')
    
    elif request.method == 'POST':
        serializer = loginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({ 'id': user.id,
        'username': user.username,
        'email': user.email,
        'token':access_token}, status = status.HTTP_200_OK)

# @api_view()
# def todo_items(request):
#     queryset = TodoItem.objects.all()
#     serializer = TodoItemSerializer(queryset, many=True)
#     return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create_todo_item(request):
    if request.method == 'GET':
        todoItem = TodoItem.objects.filter(user = request.user).order_by('-created_at')
        serializer = TodoItemSerializer(todoItem, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def delete_todo_item(request, item_id):
    return Response(f'Delete Todo Item Endpoint for item {item_id}')

@api_view(['GET','PUT', 'DELETE'])
def list_todo_items(request,id):
    todoItem = get_object_or_404(TodoItem,user =request.user,pk=id)
    if request.method == 'GET':
        serializer = TodoItemSerializer(todoItem)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoItemSerializer(todoItem, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        todoItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    