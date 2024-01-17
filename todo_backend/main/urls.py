from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='headpage'),
    path('todo_list', views.index, name='todopage'),
    path('delete_task/<int:pk>/', views.DeleteTask.as_view(), name='delete_task'),
]
