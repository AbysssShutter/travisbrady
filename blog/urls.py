from django.urls import path
from . import views

urlpatterns = [
    path(r'/blog/about', views.about, name='about'),
    path(r'/blog/contacts', views.contacts, name='contact'),
    path(r'', views.index),
]
