from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from commandcenter.views import *

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('commandcenter.urls')),
]