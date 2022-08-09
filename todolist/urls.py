from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('del/<int:todo_id>', views.delete),
    path('add/', views.add),
]