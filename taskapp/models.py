from django.db import models
from django.contrib.auth.hashers import make_password,check_password
import datetime
class User(models.Model):
    id=models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    user_type = models.CharField(max_length=100, choices=[('ADMIN', 'ADMIN'), ('MANAGER', 'MANAGER'), ('MEMBER', 'MEMBER')])
    password= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def check_password(self, raw_password):
        # Check if the provided raw password matches the hashed password
        return check_password(raw_password, self.password)
    
class Projects(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=[('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Tasks(models.Model): 
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=[('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')])
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(Projects,related_name='project', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
class projectmember(models.Model):
    id=models.BigAutoField(primary_key=True)
    project=models.ForeignKey(Projects, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   


