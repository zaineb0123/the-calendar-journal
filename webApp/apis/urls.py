
from django.urls import path, re_path
from django.contrib import admin
from webApp.apis import views

urlpatterns = [
    path("day/<str:date>", views.getDayData, name="day"),
    path("day/<str:date>/<int:dayID>/createTodo/", views.createTodoList, name="createTodoList"),
    path('day/<str:date>/<int:todoTaskID>/edit/', views.editTodoList, name="edit"),
    path('day/', views.addDay, name="addDay"),
    path('day/<str:date>/<int:todoTaskID>/remove', views.removeTodoList, name="removeTodoList"),

]

# from django.urls import include, path
# from rest_framework import routers
# from webApp.apis import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'day', views.DayViewSet)
# router.register(r'category', views.CategoryViewSet)


# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]