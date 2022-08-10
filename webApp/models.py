from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Day(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user', null=True)
    todoList = models.CharField(max_length=256)
    status = models.BooleanField(default=False)
    dayComplete = models.BooleanField(default=False)
    journal = models.CharField(max_length=2000)
    class Meta:
        db_table = "Day"

class Category(models.Model):
    categoryName = models.CharField(max_length=120)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'created_By', null=True)
    class Meta:
        db_table = "Category"

