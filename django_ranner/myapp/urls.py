from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('category', views.services, name='services'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('basket', views.basket, name='basket'),
    path('view_cart', views.Cart, name='view_cart'),
    path('checkout', views.checkout, name='checkout'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)