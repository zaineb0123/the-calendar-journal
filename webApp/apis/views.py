from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login as auth_login, logout
from django.template.defaulttags import register
from django.db import IntegrityError
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from ..models import User, Day, Category
from .serializers import UserSerializer, DaySerializer, CategorySerializer
# from apps.lib import main

# Create your views here.

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': ''
#         }
#     ]

@api_view(['GET'])
def get_day_data(request):
    day_data = Day.objects.all()
    serializer = DaySerializer(day_data, many=True)
    return Response(day_data)


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


