from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='headpage'),
    path('todo_list', views.index, name='todopage'),
]
