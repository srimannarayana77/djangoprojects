from django.urls import path
from taskapp.controllers.taskControllers import TasksCreateView

urlpatterns = [
path('', TasksCreateView.post),
path('all', TasksCreateView.get),
path('<int:id>', TasksCreateView.getSingle),
path('<int:id>/update', TasksCreateView.put),
path('<int:id>/delete', TasksCreateView.delete),
path('fakedata',TasksCreateView.fakedata),
]
