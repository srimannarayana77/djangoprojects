from django.urls import path
from taskapp.controllers.userControllers import UserCreateView,UserSignInView

urlpatterns = [
path('',UserCreateView.post),
path('all', UserCreateView.get),
path('<int:id>', UserCreateView.getSingle),
path('<int:id>/update', UserCreateView.put),
path('<int:id>/delete', UserCreateView.delete),
path('signin',UserSignInView.signin)
]
