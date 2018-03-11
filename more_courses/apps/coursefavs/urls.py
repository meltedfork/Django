from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/favorite$', views.favorite),
    url(r'^(?P<id>\d+)/popfavback$', views.popfavback),
    url(r'^(?P<id>\d+)/remove$', views.remove),
    url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^logout$', views.logout)
]    
