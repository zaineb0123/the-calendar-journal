
# from django.urls import path, re_path
# from django.contrib import admin
# from webApp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", views.homePage, name="homePage"),
#     path("login", views.login, name="login"),
#     path("register", views.register, name="register"),
#     path("calendar", views.calendar, name="calendar"),
#     path("day", views.day, name="day")
# ]

from django.urls import include, path
from rest_framework import routers
from webApp import views
from webApp.apis import urls

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'day', views.DayViewSet)
# router.register(r'category', views.CategoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('webApp.apis.urls')),
]