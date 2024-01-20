from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]
