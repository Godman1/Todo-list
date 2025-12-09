from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import TodoItemListCreate, ListTodoItems,RegisterUserView,LoginView
from . import views



urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),  
    path('login/',  LoginView.as_view(), name='login'),  
    # path('todo/', views.todo_items, name='todo_items'),
    path('todo/', TodoItemListCreate.as_view(), name='todo_items'),
    path('todo/<int:id>/', ListTodoItems.as_view(), name='list_todo_items'),
   
]