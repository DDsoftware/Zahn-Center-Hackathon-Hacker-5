from django.conf.urls import url
from hacker5 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]