from django.conf.urls import patterns, url

from tasks import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<task_id>[^/]+)/', views.alter, name='alter'),
)
