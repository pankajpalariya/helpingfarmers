from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register/succ/', views.succ, name='succ'),
    path('login/done/', views.done, name='done'),
    path('done/', views.done, name='done'),

]
