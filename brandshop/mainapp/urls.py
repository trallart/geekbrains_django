# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url




urlpatterns = [
    # url(r'products/(?P<categories_id>\D{3,})/$', views.products, name='products'),
    # url(r'products/(?P<categories_id>\D{3,})/(?P<brand_id>\D{3,})/$', views.brand_filter, name='brand_filter'),
    # url(r'^sort/(?P<name>\D{2,})/', views.sortby, name='sortby'),

    url(r'products/(?P<categories_id>\D{3,})/(?P<catalog_id>\D{0,})/(?P<brand_id>\D{3,})/$', views.brand_filter, name='brand_filter'),
    # url(r'products/(?P<categories_id>\D{3,})/(?P<brand_id>\D{3,})/$', views.brand_filter, name='brand_filter'),
    url(r'products/(?P<categories_id>\D{3,})/(?P<catalog_id>\D{3,})/$', views.catalog_filter, name='catalog_filter'),
    url(r'products/(?P<categories_id>\D{3,})/', views.products, name='products'),
    # url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^single/', views.single_page, name='single_page'),

    url(r'^$', views.main, name='main'),
]