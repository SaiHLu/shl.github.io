from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create, name="create"),
    path('<int:todo_id>/', views.edit, name="edit"),
    path('<int:todo_id>/update', views.update, name="update"),
    path('<int:todo_id>/delete', views.delete_task, name="delete_task"),
]
