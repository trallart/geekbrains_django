# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpattenrns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    # url(r'^$', views.index, name='index')
    url(r'^$', views.main, name='main'),
    url(r'products/(?P<categories_id>\D{3,})/$', views.products, name='products'),
    # url(r'products/men', views.products, name='products'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^single/', views.single_page, name='single_page'),
]