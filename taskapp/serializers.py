from rest_framework import serializers
from .models import User,Projects,Tasks,projectmember

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields = ('first_name', 'last_name', 'email', 'id', 'user_type', 'password', 'created_at', 'updated_at')
  extra_kwargs = {
'password': {'write_only': True},
'user_id': {'read_only': True},
'created_at': {'read_only': True},
'updated_at': {'read_only': True},
}

class fakeuserserializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields = ('first_name', 'last_name', 'email', 'id', 'user_type')


class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ('id','title','description','user','start_date','end_date','status','created_at','updated_at')

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
   model=Projects
   fields=('id','title','description','user','start_date','end_date','status')

class TasksSerializer(serializers.ModelSerializer):
  # project =ProjectsSerializer()
  # created_by=UserSerializer()
  class Meta:
   model = Tasks
   fields = '__all__'

class projectmemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = projectmember
    fields = '__all__'
