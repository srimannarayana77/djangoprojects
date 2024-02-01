# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView
# from .models import User,Projects,Tasks,projectmember
# from .serializers import UserSerializer,ProjectsSerializer,TasksSerializer,projectmemberSerializer
# from .messages import *


# class UserCreateView(APIView):
#  def post(self, request):
#     try:
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#          serializer.save()
#         return Response({'success': True, 'message':CREATE_USER_SUCCESSFULLY , 'data':serializer.data}, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#  def get(self,request,id=None):
#     try:
#        if id is None:
#           users = User.objects.all()
#           serializer = UserSerializer(users, many=True)
#           return Response({'success': True, 'message':ALL_USERS_RETRIVE_SUCCESSFULLY , 'data':serializer.data})
#        else:
#           user_by_id = get_object_or_404(User, id= id)
#           serializer = UserSerializer(user_by_id)
#           return Response({'success': True, 'message':SINGLE_USER_RETRIVE_SUCCESSFULLY , 'data':serializer.data})
#     except Exception as e:
#           return Response({"error": e.detail}, status=e.status_code)
    
#  def put(self,request, id):
#       try:
#         user_update = User.objects.get(id=id) 
#         serializer = UserSerializer(user_update, data=request.data) 
#         if serializer.is_valid():
#           serializer.save() 
#           return Response({'success': True, 'message':UPDATE_USER_SUCCESSFULLY , 'data':serializer.data})
#       except Exception as e:
#           return Response({"error": e.detail}, status=e.status_code)
      
#  def delete(self,request, id):
#       try:
#         user_delete = User.objects.get(id=id)
#         user_delete.delete() 
#         return Response({'success': True, 'message': DELETE_USER_SUCCESSFULLY})
#       except Exception as e:
#         return Response({"error": e.detail}, status=e.status_code)


# class UserSignInView(APIView):
#   def post(self, request):
#         try:
#             username = request.data.get('', None)
#             print("usename----",username)
#             password = request.data.get('password', None)
#             print('password---',password)

#             user = None
#             if '@' in username:
#                 try:
#                     user = User.objects.get(email=username)
#                     print('user---',user)
#                 except User.DoesNotExist:
#                     pass

#             if not user:
#                 user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 token, created = Token.objects.get_or_create(user=user)
#                 serializer = UserSerializer(user)
#                 return Response({
#                     'success': True,
#                     'message': 'User signed in successfully.',
#                     'data': serializer.data,
#                     'token': token.key
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Authentication failed."}, status=status.HTTP_401_UNAUTHORIZED)

#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class ProjectsCreateView(APIView):
#    def post(self, request):
#     try:
#         serializer = ProjectsSerializer(data=request.data)
#         if serializer.is_valid():
#          serializer.save()
#         return Response({'success': True, 'message':CREATE_A_PROJECT_SUCCESSFULLY , 'data':serializer.data}, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"error": e.detail}, status=e.status_code)
    
#    def get(self,request,id=None):
#     try:
#        if id is None:
#           projects = Projects.objects.all()
#           serializer = ProjectsSerializer(projects, many=True)
#           return Response({'success': True, 'message':ALL_PROJECTS_RETRIVE_SUCCESSFULLY, 'data':serializer.data})
#        else:
#           project_by_id = get_object_or_404(Projects, id= id)
#           serializer = ProjectsSerializer(project_by_id)
#           return Response({'success': True, 'message':SINGLE_PROJECT_RETRIVE_SUCCESSFULLY , 'data':serializer.data})
#     except Exception as e:
#           return Response({"error": e.detail}, status=e.status_code) 
    
#    def put(self,request, id):
#       try:
#         project_update = Projects.objects.get(id=id) 
#         serializer = ProjectsSerializer(project_update, data=request.data) 
#         if serializer.is_valid():
#           serializer.save() 
#           return Response({'success': True, 'message':UPDATE_A_PROJECT_SUCCESSFULLY , 'data':serializer.data})
#       except Exception as e:
#           return Response({"error": e.detail}, status=e.status_code)
      
#    def delete(self,request, id):
#       try:
#         project_delete = Projects.objects.get(id=id)
#         project_delete.delete() 
#         return Response({'success': True, 'message': DELETE_A_PROJECT_SUCCESSFULLY})
#       except Exception as e:
#         return Response({"error": e.detail}, status=e.status_code)
      

# class TasksCreateView(APIView):
#    def post(self, request):
#     try:
#         serializer = TasksSerializer(data=request.data)
#         if serializer.is_valid():
#          serializer.save()
#         return Response({'success': True, 'message':CREATE_A_PROJECT_SUCCESSFULLY , 'data':serializer.data}, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"error": e.detail}, status=e.status_code)
    
#    def get(self,request,id=None):
#     try:
#        if id is None:
#           tasks = Tasks.objects.all()
#           serializer = TasksSerializer(tasks, many=True)
#           return Response({'success': True, 'message':ALL_TASKS_RETRIVE_SUCCESSFULLY, 'data':serializer.data})
#        else:
#           task_by_id = get_object_or_404(Tasks, id= id)
#           serializer = TasksSerializer(task_by_id)
#           return Response({'success': True, 'message':SINGLE_TASK_RETRIVE_SUCCESSFULLY , 'data':serializer.data})
#     except Exception as e:
#           return Response({"error": e.detail}, status=e.status_code) 
    
#    def put(self,request, id):
#       try:
#         task_update = Tasks.objects.get(id=id) 
#         serializer = TasksSerializer(task_update, data=request.data) 
#         if serializer.is_valid():
#           serializer.save() 
#           return Response({'success': True, 'message':UPDATE_A_TASKS_SUCCESSFULLY , 'data':serializer.data})
#       except Exception as e:
#           return Response({"error": e.detail}, status=e.status_code)
      
#    def delete(self,request, id):
#       try:
#         task_delete = Tasks.objects.get(id=id)
#         task_delete.delete() 
#         return Response({'success': True, 'message': DELETE_A_TASKS_SUCCESSFULLY})
#       except Exception as e:
#         return Response({"error": e.detail}, status=e.status_code)
   
# class ProjectmemberView(APIView):
#    def post(self, request):
#     try:
#         serializer = projectmemberSerializer(data=request.data)
#         if serializer.is_valid():
#          serializer.save()
#         return Response({'success': True, 'message':CREATE_A_PROJECT_MEMBER_SUCCESSFULLY , 'data':serializer.data}, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({"error": e.detail}, status=e.status_code)
      
#    def delete(self,request, id):
#       try:
#         task_delete = projectmember.objects.get(id=id)
#         task_delete.delete() 
#         return Response({'success': True, 'message': DELETE_A_PROJECT_MEMBER_SUCCESSFULLY})
#       except Exception as e:
#         return Response({"error": e.detail}, status=e.status_code)