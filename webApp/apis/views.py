from django.shortcuts import render
import json
from datetime import date
from django.contrib.auth import authenticate, login as auth_login, logout
from django.template.defaulttags import register
from django.db import IntegrityError
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from ..models import User, Day, Category, TodoList
from .serializers import UserSerializer, DaySerializer, CategorySerializer, TodoListSerializer, DayTodoListSerializer
from allauth.account.decorators import login_required


# from apps.lib import main

# Create your views here.

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': ''
#         }
#     ]


@login_required
@api_view(['GET'])
def getDayData(request, date):
    user = request.user
    data = Day.objects.get(date=date, userID=user)
<<<<<<< HEAD
=======

>>>>>>> main
    dayserializer = DaySerializer(data, many=False)
    todoEntries = TodoList.objects.filter(dayID=data.id)
    todoListSerializer = TodoListSerializer(todoEntries, many=True)

    return Response({
        "Day":dayserializer.data,
        "todoList":todoListSerializer.data
    })

@login_required
@api_view(['POST'])
def addDay(request):
    user = request.user
    today = date.today()
    dayEntry = Day.objects.create(
        userID=user,
        date=today
    )
    serializer = DaySerializer(dayEntry, many=False)
    return Response(serializer.data)

@login_required
@api_view(['POST'])
def createTodoList(request, date, dayID):
    data = request.data
    dayEntry = Day.objects.get(id=dayID)
    print(dayEntry.id)

    if dayEntry:
        todoEntry = TodoList.objects.create(
            todoTask=data['todoTask'],
            dayID = dayEntry, 
        )
        serializer = TodoListSerializer(todoEntry, many=False)
        return Response(serializer.data)
    else:
        print("Error")

@login_required
@api_view(['PUT'])
def editTodoList(request, date, todoTaskID):
    todoTask = TodoList.objects.get(id=todoTaskID)   
    serializer = TodoListSerializer(todoTask, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
    
@api_view(['DELETE'])
def removeTodoList(request, date, todoTaskID):
    todoTask = TodoList.objects.get(id=todoTaskID)  
    todoTask.delete()
    return Response('Note entry has been deleted!') 


@login_required
@api_view(['PUT'])
def dayUpdate(request, date, dayID):
    dayEntry = Day.objects.get(id=dayID)   
    serializer = DaySerializer(dayEntry, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
    
    
# @api_view(['DELETE'])
# def removeJournalEntry(request, date, dayID):
#     dayEntry = Day.objects.get(id=dayID)   
#     dayEntry.delete()
#     return Response('Journal entry has been deleted!') 

# def homePage(request):
#     return render(request, "main.dart")

# @api_view(['GET', 'POST'])
# def login(request):
#     if request.method == "POST":
#         print("inside post")
#         # Attempt to sign user in
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         print("user value ", user)
#         # Check if authentication successful
#         if user is not None:
#             auth_login(request, user)
#             print("i should go to calendar now")
#             return HttpResponseRedirect(reverse("calendar"))
#         else:
#             return render(request, "login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "login.html")
   
# def register(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         print("Username is ", username)
#         print("Email is ", email)
#         # Ensure password matches confirmation
#         password = request.POST.get("password")
#         confirmation = request.POST.get("confirmation")
#         if password != confirmation:
#             return render(request, "register.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
            
#         except IntegrityError:
#             return render(request, "register.html", {
#                 "message": "Username already taken."
#             })
    
#         auth_login(request, user)
#         return HttpResponseRedirect(reverse("login"))
#     else:
#         return render(request, "register.html")
    

# def calendar(request):
#     return render(request, "calendar.html")

# def day(request):
#     return render(request, "day.html")


