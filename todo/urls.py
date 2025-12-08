from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register_user, name='register'),  
    path('login/', views.login_user, name='login'),  
    # path('todo/', views.todo_items, name='todo_items'),
    path('todo/', views.create_todo_item, name='create_todo_item'),
    path('todo/<int:id>/', views.list_todo_items, name='list_todo_items'),
   
]