from django.urls import path
from .views import DetailTodo, CreateTodo, DeleteTodo
from . import views

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view()),
     path("tasks/", views.get_tasks),
    path("tasks/stats/", views.productivity_stats),
]