from django.urls import path
#importar desde la ruta actual
from . import views

urlpatterns = [
    # Al ejecutar la ruta inicial se ejecuta
    path('', views.index, name = "index"), 
    path('about/', views.about, name = "about"), 
    # la ruta espera una string
    path('hello/<str:username>', views.hello, name = "hello"), 
    path('projects/', views.projects, name = "projects"), 
    path('projects/<int:id>', views.project_detail, name = "project_detail"), 
    path('tasks/', views.tasks, name = "tasks"), 
    path('create_task/', views.create_task, name = "create_task"),
    path('create_project/', views.create_project, name = "create_project"),
]