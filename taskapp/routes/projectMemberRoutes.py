from django.urls import path
from taskapp.controllers.projectMemberController import ProjectmemberView

urlpatterns = [
path('', ProjectmemberView.post),
path('all', ProjectmemberView.get),
path('<int:id>', ProjectmemberView.getSingle),
path('<int:id>/update', ProjectmemberView.put),
path('<int:id>/delete', ProjectmemberView.delete),
]