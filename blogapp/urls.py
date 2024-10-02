from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('add_blog/',views.add_blogs, name="add_blogs"),
    path('',views.showblog,name="showblog"),
    path('add_comment/<int:id>',views.add_comment, name="add_comment")
]
