from django.conf.urls import url

from django.urls import path

from . import views

# app_name = 'authapp'

urlpatterns = [
    # path('', views.LoginView.as_view(), name='login'),

    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('edit/', views.edit, name = 'edit'),

    path('',  views.login, name='login'),
]