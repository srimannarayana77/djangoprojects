import jwt
from django.conf import settings
from rest_framework.response import Response
from functools import wraps
from taskapp.models import User

def decode_jwt_token(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        print('auth=', auth_header)
        try:
            decoded_data = jwt.decode(jwt=auth_header, key=settings.SECRET_KEY,algorithms=["HS256"])
            print('decode=',decoded_data)
            user_id = decoded_data['user_id'] 
            # Fetch user details from the database
            user_details = User.objects.filter(id=decoded_data['user_id']).values()
            print('user_details=', user_details)
            print(type(user_details))
            if user_details:
                user_type = user_details[0].get('user_type')
                print('usertype=', user_type)
                request.user_type = user_type  # Add user_type to request for later use
                return view_func(request, *args, **kwargs)
            else:
                return Response({'success': False, 'message': 'User details not found'}, status=404)
        except jwt.ExpiredSignatureError:
            return Response({'success': False, 'message': 'Token has expired'}, status=401)
        except jwt.DecodeError:
            return Response({'success': False, 'message': 'Require Token'}, status=422)     
    return _wrapped_view


def allow_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        decoded_data = decode_jwt_token(request)
        print('decoded=',decoded_data)
        user_type = decoded_data.__getattribute__('user_type')
        if user_type == 'ADMIN':
            return view_func(request, *args, **kwargs)
        else:
            return Response({'success': False, 'message': 'You do not have permission to create projects.'}, status=401)

    return _wrapped_view

def allow_member(view_func):
    def _wrapped_view(request, *args, **kwargs):
        decoded_data = decode_jwt_token(request)
        print('decoded=',decoded_data)
        user_type = decoded_data.__getattribute__('user_type')
        if user_type == 'MEMBER':
            return view_func(request, *args, **kwargs)
        else:
            return Response({'success': False, 'message': 'You do not have permission to create tasks.'}, status=401)

    return _wrapped_view

def allow_manager(view_func):
    def _wrapped_view(request, *args, **kwargs):
        decoded_data = decode_jwt_token(request)
        print('decoded=',decoded_data)
        user_type = decoded_data.__getattribute__('user_type')
        if user_type == 'MANAGER':
            return view_func(request, *args, **kwargs)
        else:
            return Response({'success': False, 'message': 'You do not have permission to create projectmembers.'}, status=401)

    return _wrapped_view