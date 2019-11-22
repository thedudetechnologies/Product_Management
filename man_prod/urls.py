from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('index/',views.index , name='index'),
    path('add/',views.add_product , name='add_product'),
    path('category/',views.category , name='categories'),
    path('crud/',views.crud , name='table'),
    path('update/',views.updates , name='update'),
    path('deletes/',views.deletes , name='deletes'),
]
