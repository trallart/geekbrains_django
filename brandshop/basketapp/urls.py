from django.conf.urls import url

from django.urls import path, re_path

from . import views


urlpatterns = [
    re_path(r'^add/(?P<pk>\d+)/$', views.basket_add, name='basket_add'),  #  Добавление товара в корзину
    re_path(r'^remove/(?P<pk>\d+)/$', views.basket_remove, name='basket_remove'),  # Удаление товара из корзины
    path('', views.basket, name = 'basket'),  # Просмотр корзины
]