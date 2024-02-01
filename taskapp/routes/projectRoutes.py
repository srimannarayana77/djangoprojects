from django.urls import path
from taskapp.controllers.projectControllers import ProjectsCreateView

urlpatterns = [
path('', ProjectsCreateView.post),
path('all', ProjectsCreateView.get),
path('<int:id>', ProjectsCreateView.getSingle),
path('<int:id>/update', ProjectsCreateView.put),
path('<int:id>/delete', ProjectsCreateView.delete),  
]

