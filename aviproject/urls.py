from django.contrib import admin
from django.urls import path
from .views import my_first_api

urlpatterns =[
    path('admin/', admin.site.urls),
    path('hello/',my_first_api),
]