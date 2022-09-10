from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    firstName = models.CharField(max_length=30, null=True, blank=True)
    lastName = models.CharField(max_length=30, null=True, blank=True)

class Category(models.Model):
    categoryName = models.CharField(max_length=120)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'created_By', null=True)
    class Meta:
        db_table = "Category"


class Day(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user', null=True)
    status = models.BooleanField(default=False)
    dayComplete = models.BooleanField(default=False)
    journal = models.CharField(max_length=2000, null=True, blank=True)
    date = models.DateField(auto_now=True, blank=True)
    # todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name = 'todoList', null=True)

    class Meta:
        db_table = "Day"

class TodoList(models.Model):
    todoTask = models.CharField(max_length=1000, null=True, blank=True)
    dayID = models.ForeignKey(Day, on_delete=models.CASCADE, related_name = 'day_id', null=True) 

    class Meta:
        db_table = "TodoList"