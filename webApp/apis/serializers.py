# from django.contrib.auth.models import User
from webApp.models import User, Day, Category, TodoList
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'firstName', 'lastName']

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = [
        'userID',
        'dayComplete',
        'journal', 
        'date'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryName', 'createdBy']

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['todoTask', 'dayID', 'status',]

class DayTodoListSerializer(serializers.ModelSerializer):
    lists = serializers.SerializerMethodField()

    class Meta:
        model = Day
        fields = '__all__'
    
    def getTodoList(self, obj):
        data = TodoListSerializer(obj.lists.all(), many=True).data
        return data