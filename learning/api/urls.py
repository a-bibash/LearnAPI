from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home),
    path('post-student/', post_student)
]
