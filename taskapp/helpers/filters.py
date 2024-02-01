from django.db.models import Q
from taskapp.models import *

def user_filters(users,params):
 try:
    filters = Q()
    first_name = params.get('first_name') 
    user_type = params.get('user_type')
    email = params.get('email')
    if first_name:
        filters &= Q(first_name__icontains=first_name)
    if user_type:
        filters &= Q(user_type=user_type)
    if email:
        filters &= Q(email=email)
    return users.filter(filters)
 except Exception as e:
        print("er",e)
        raise e
 
def project_filters( projects,params):
    
 try:
        filters = Q()
        title = params.get('title', None)  # Apply filters based on query parameters
        description = params.get('description', None)
        user = params.get('user', None)
        status = params.get('status', None)
        
        if title:
            filters &= Q(title__icontains=title)
        if description:
            filters &= Q(description__icontains=description)
        if user:
            filters &= Q(user=user)
        if status:
            filters &= Q(status=status)
        return projects.filter(filters)
 except Exception as e:
        print("er",e)
        raise e

def task_filters(tasks,params ):
 try:
    filters = Q()
    name = params.get('name', None)
    description = params.get('description', None)
    status =params.get('status', None)
    start_date = params.get('start_date', None)
    end_date = params.get('end_date', None)
    project =params.get('project', None)
    created_by = params.get('created_by', None)

    if name:
        filters &= Q(name__icontains=name)
    if description:
        filters &= Q(description__icontains=description)
    if status:
        filters &= Q(status=status)
    if start_date:
        filters &= Q(start_date=start_date)
    if end_date:
        filters &= Q(end_date=end_date)
    if project:
        filters &= Q(project=project)
    if created_by:
        filters &= Q(created_by=created_by)

    return tasks.filter(filters)
 except Exception as e:
        print("er",e)
        raise e

def project_member_filters(project_members, params):
  try:
      filters = Q()
      project_id = params.get('project_id', None) # Extract filter parameters from request
      user_id = params.get('user_id', None)
      is_active =params.get('is_active', None)

      if project_id:
            filters &= Q(project=project_id)
      if user_id:
            filters &= Q(user=user_id)
      if is_active is not None:
            filters &= Q(is_active=is_active)

      return project_members.filter(filters)
  except Exception as e:
        print("er",e)
        raise e 
