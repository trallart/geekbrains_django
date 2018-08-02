# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url




urlpatterns = [
    # url(r'^$', views.index, name='index')
    # url(r'#openModal', views.admines, name='#openModal'),
    url(r'^$', views.main, name='main'),
    url(r'products/(?P<categories_id>\D{3,})/$', views.products, name='products'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^single/', views.single_page, name='single_page'),


]