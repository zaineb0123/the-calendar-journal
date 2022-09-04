# from django.contrib.auth.models import User
from webApp.models import User, Day, Category
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = [
        'posted_by',
        'todoList',
        'status',
        'dayComplete',
        'journal'
        ]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryName', 'createdBy']