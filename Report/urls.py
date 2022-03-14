
from django import views
from django.contrib import admin
from django.urls import path
from Core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage, name='home')
]
