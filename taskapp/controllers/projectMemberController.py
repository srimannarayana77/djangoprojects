from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import serializers
import jwt
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from taskapp.helpers.paginations import paginationResponse
from rest_framework import viewsets
from taskapp.helpers.filters import project_member_filters
from taskapp.helpers.sort import sort_projectmembers
from taskapp.middlewares.decorators import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.decorators import api_view
from taskapp.models import projectmember,User
from rest_framework.exceptions import ValidationError
from taskapp.serializers import projectmemberSerializer
from taskapp.messages import *

class ProjectmemberView(viewsets.ViewSet):
   @api_view(['POST'])
   @decode_jwt_token
   @allow_manager
   def post(request):
    try:
        
            serializer = projectmemberSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'message':CREATE_A_PROJECT_MEMBER_SUCCESSFULLY , 'data':serializer.data}, status=201)

    except serializers.ValidationError as e:
            return Response({'success': False, 'message': e.detail}, status=422)
    except projectmember.DoesNotExist:
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
            project_members = projectmember.objects.all()
            project_members = project_member_filters( project_members,request.query_params)
            project_members= sort_projectmembers(sortBy, sortType, project_members)
            page_result = paginator.paginate_queryset(project_members, request)
            serializer = projectmemberSerializer(page_result, many=True)
            Response_Data = paginationResponse(ALL_USERS_RETRIVE_SUCCESSFULLY ,paginator.page.paginator.count, limit, page, serializer.data)
            return Response(Response_Data, status=200)
        
        except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)

   @api_view(['GET'])
   @decode_jwt_token
   def getSingle(request, id):
        try:
            project_member = projectmember.objects.get(id=id)
            serializer = projectmemberSerializer(project_member)
            return Response({'success': True, 'message': SINGLE_PROJECT_MEMBER_RETRIEVE_SUCCESSFULLY, 'data': serializer.data}, status=200)
        except projectmember.DoesNotExist:
            return Response({'success': False, 'errors': PROJECT_MEMBER_NOT_FOUND}, status=404)
        except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)

   @api_view(['PUT'])
   @decode_jwt_token
   @allow_manager
   def put(request, id):
        try:
            project_member = projectmember.objects.get(id=id)
            serializer = projectmemberSerializer(project_member, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'success': True, 'message': UPDATE_PROJECT_MEMBER_SUCCESSFULLY, 'data': serializer.data}, status=200)
        except serializers.ValidationError as e:
                return Response({'success': False, 'errors': e.detail}, status=422)
        except projectmember.DoesNotExist:
            return Response({'success': False, 'errors': PROJECT_MEMBER_NOT_FOUND}, status=404)
        except Exception as err: 
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)
    
   @api_view(['DELETE']) 
   @decode_jwt_token
   @allow_manager 
   def delete(request, id):
      try:
        task_delete = projectmember.objects.get(id=id)
        task_delete.delete() 
        return Response({'success': True, 'message': DELETE_A_PROJECT_MEMBER_SUCCESSFULLY},status=204)
      except projectmember.DoesNotExist:
            return Response({'success': False, 'message': PROJECT_MEMBER_NOT_FOUND}, status=404)
      except Exception as err:
            error_message = str(err)
            return Response({'success': False, 'errors': error_message}, status=500)