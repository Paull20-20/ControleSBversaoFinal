from django.urls import path

from . import views

#aqui criamos nossas urls com o path

#Na url http://127.0.0.1:8000/admin/ o user e pass é root, criamos via terminal! e-mail dele é o empresarial

#continuar aula apartir de: https://www.youtube.com/watch?v=npaSyVGE93g&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=11

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('painel/', views.painel, name='painel'),
    
    
]



