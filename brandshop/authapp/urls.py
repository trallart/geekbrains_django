from django.conf.urls import url

from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout')
]