from rest_framework import status
import jwt
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import api_view
from taskapp.helpers.paginations import paginationResponse
from taskapp.helpers.filters import project_filters
from taskapp.helpers.sort import sort_projects
from taskapp.middlewares.decorators import *
from taskapp.models import Projects
from taskapp.serializers import ProjectsSerializer
from taskapp.messages import *

class ProjectsCreateView(viewsets.ViewSet):
   @api_view(['POST'])
   @decode_jwt_token
   @allow_admin  
   def post(request):
    try:   
           
          #  title = request.data.get('title')
          #  description=request.data.get('description')
           user=request.data.get('user')
           if Projects.objects.filter(user=user).exists():
             return Response({'success': False, 'message': 'A project with this user  already exists.'}, status=400)      
           serializer = ProjectsSerializer(data=request.data)
           print("serializer=",serializer)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response({'success': True, 'message':CREATE_A_PROJECT_SUCCESSFULLY ,'data':serializer.data}, status=201)
    except serializers.ValidationError as e:
                return Response({'success': False, 'message': e.detail}, status=422)
    except Projects.DoesNotExist:
        return Response({'success': False, 'message': USER_NOT_FOUND}, status=404)    
    except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
    
   @api_view(['GET']) 
   @decode_jwt_token
   def get(request):
    try:  
          paginator = PageNumberPagination()
          limit = int(request.query_params.get('limit', 2))
          page = int(request.query_params.get('page', 1))
          paginator.page_size = limit
          sortBy = request.query_params.get('sort_by', 'id')
          sortType = request.query_params.get('sort_type', 'desc')
          
          projects = Projects.objects.all()
          projects = project_filters(projects,request.query_params)
          projects = sort_projects(sortBy, sortType, projects)
          page_result = paginator.paginate_queryset(projects, request)
          serializer = ProjectsSerializer(page_result, many=True)
          Response_Data = paginationResponse(ALL_USERS_RETRIVE_SUCCESSFULLY ,paginator.page.paginator.count, limit, page, serializer.data)
          return Response(Response_Data,status=200) 
    except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message},  status=500)
    
   @api_view(['GET'])
   @decode_jwt_token 
   def getSingle(request,id):
    try:    
          project_by_id = Projects.objects.get(id= id)
          serializer = ProjectsSerializer(project_by_id)
          return Response({'success': True, 'message':SINGLE_PROJECT_RETRIVE_SUCCESSFULLY , 'data':serializer.data},status=200)
    except Projects.DoesNotExist:
            return Response({'success': False, 'message':PROJECT_NOT_FOUND}, status=404)
    except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
    
   
   @api_view(['PUT'])
   @decode_jwt_token
   @allow_admin 
   def put(request, id):
      try:
        project_update = Projects.objects.get(id=id) 
        serializer = ProjectsSerializer(project_update, data=request.data) 
        if serializer.is_valid(raise_exception=True):
          serializer.save() 
          return Response({'success': True, 'message':UPDATE_A_PROJECT_SUCCESSFULLY , 'data':serializer.data},status=200)
      except serializers.ValidationError as e:
                return Response({'success': False, 'message': e.detail}, status=422)
      except Projects.DoesNotExist:
            return Response({'success': False, 'message': PROJECT_NOT_FOUND}, status=404)
      except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
   
   @api_view(['DELETE']) 
   @decode_jwt_token
   @allow_admin 
   def delete(request, id):
      try: 
        project_delete = Projects.objects.get(id=id)
        project_delete.delete() 
        return Response({'success': True, 'message': DELETE_A_PROJECT_SUCCESSFULLY}, status=204)
      except Projects.DoesNotExist:
        return Response({'success': False, 'message': PROJECT_NOT_FOUND }, status=404)
      except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)