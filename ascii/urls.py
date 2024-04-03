from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_view, name='upload_form'),
    path('images', views.image_view, name='images'),
] 