from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),  # List all tasks
    path('update/<str:pk>/', views.updateTask, name="update_task"),  # Update task
    path('delete/<str:pk>/', views.deleteTask, name="delete_task"),  # Delete task
]
