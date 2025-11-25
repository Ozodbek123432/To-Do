from django.db import models
from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    duo_date = models.DateField(null = True, blank = True)

class ToDoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length= 50)
    password1 = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
