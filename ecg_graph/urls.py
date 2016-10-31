from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^submit/', views.submit, name='submit'),
    url(r'^list/', views.list, name='list'),
    url(r'^(?P<data_id>[0-9]+)/graph/$', views.graph, name='graph'),
    url(r'^$', views.list, name='list'),
]
