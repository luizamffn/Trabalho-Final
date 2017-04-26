from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^play/$', views.play, name='play'),
    url(r'^stop/$', views.stop, name='stop'),
    url(r'^add/$', views.add, name='add'),
    url(r'^list/$', views.list, name='list'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.delete, name='delete'),
]