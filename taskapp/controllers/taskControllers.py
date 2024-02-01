from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import ObtainAuthToken
import jwt
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from taskapp.helpers.paginations import paginationResponse
from taskapp.helpers.filters import task_filters
from taskapp.helpers.sort import sort_tasks
from taskapp.middlewares.decorators import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from taskapp.models import Tasks,User
from taskapp.serializers import TasksSerializer
from taskapp.fakers import generate_fake_tasks
from taskapp.messages import *

class TasksCreateView(viewsets.ViewSet):
   @api_view(['POST'])
   @decode_jwt_token
   @allow_member
   def post(request):
    try: 
        task_data = request.data
        existing_task = Tasks.objects.filter(
        name=task_data.get('name'),
        description=task_data.get('description')).first()
        if existing_task:
          return Response({'message': 'Task with similar characteristics already exists.'}, status=400)
        serializer = TasksSerializer(data=task_data)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response({'success': True, 'message':CREATE_A_TASKS_SUCCESSFULLY , 'data':serializer.data}, status=201)
    except serializers.ValidationError as e:
                return Response({'success': False, 'message': e.detail}, status=422)       
    except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
    
   @api_view(['GET'])
   @decode_jwt_token
   def get(request):
    try:  
          paginator = PageNumberPagination()
          limit = int(request.query_params.get('limit', 10))
          page = int(request.query_params.get('page', 1))
          paginator.page_size = limit     
          sortBy = request.query_params.get('sort_by', 'id')
          sortType = request.query_params.get('sort_type', 'desc')
          tasks = Tasks.objects.all()
          tasks= task_filters(tasks, request.query_params)
          tasks = sort_tasks(sortBy, sortType, tasks)

          page_result = paginator.paginate_queryset(tasks, request)
          serializer = TasksSerializer(page_result, many=True)
          Response_Data = paginationResponse(ALL_USERS_RETRIVE_SUCCESSFULLY ,paginator.page.paginator.count, limit, page, serializer.data)
          return Response(Response_Data,status=200)

    except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
    
   @api_view(['GET'])
   @decode_jwt_token
   def getSingle(request,id):
    try:  
          task_by_id = Tasks.objects.get(id= id)
          serializer = TasksSerializer(task_by_id)
          return Response({'success': True, 'message':SINGLE_TASK_RETRIVE_SUCCESSFULLY , 'data':serializer.data},status=200)
    except Tasks.DoesNotExist:
            return Response({'success': False, 'meassage': TASK_NOT_FOUND}, status=404)
    except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message},  status=500)
    
   @api_view(['PUT']) 
   @decode_jwt_token
   @allow_member
   def put(request, id):
      try:
        task_update = Tasks.objects.get(id=id) 
        serializer = TasksSerializer(task_update, data=request.data) 
        if serializer.is_valid(raise_exception=True):
          serializer.save() 
          return Response({'success': True, 'message':UPDATE_A_TASKS_SUCCESSFULLY , 'data':serializer.data},status=200)
      except serializers.ValidationError as e:
                return Response({'success': False, 'message': e.detail}, status=422)
      except Tasks.DoesNotExist:
            return Response({'success': False, 'errors': TASK_NOT_FOUND}, status=404)
      except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
      
   @api_view(['DELETE'])  
   @decode_jwt_token
   @allow_member 
   def delete(request, id):
      try:
        task_delete = Tasks.objects.get(id=id)
        task_delete.delete() 
        return Response({'success': True, 'message': DELETE_A_TASKS_SUCCESSFULLY}, status=204)
      except Tasks.DoesNotExist:
        return Response({'success': False, 'errors': TASK_NOT_FOUND}, status=404)
      except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
      
   @api_view(['POST'])
   @decode_jwt_token
   @allow_member
   def fakedata(request):
      try:
          num_fake_tasks = 100
          fake_tasks = generate_fake_tasks(num_fake_tasks)
          for fake_task in fake_tasks:
           fake_task.save()
          return Response({'success': True, 'message': f"{num_fake_tasks} fake tasks created successfully"})
      except Exception as err:
          error_message = str(err)
          return Response({'success': False, 'errors': error_message}, status=500)