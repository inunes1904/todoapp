from django.urls import path
from .views import index, todos, add_todo

urlpatterns = [
    path('', index, name='index'),
    path('todos/', todos, name='todos'),
    path('add_todo/', add_todo, name='add_todo')
    ]