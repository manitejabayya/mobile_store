from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'), 
    path('services.html', views.services, name='services'),
    path('contact.html', views.contact, name='contact'),
    path('accounts/', include('accounts.urls')),
]