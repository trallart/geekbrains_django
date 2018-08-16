# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url




urlpatterns = [
    url(r'products/(?P<categories_id>\D{3,})/(?P<catalog_id>\D{3,})/$', views.catalog_filter, name='catalog_filter'),
    url(r'products/(?P<categories_id>\D{3,})/', views.products, name='products'),
    url(r'^single/', views.single_page, name='single_page'),
    url(r'^$', views.main, name='main'),
]