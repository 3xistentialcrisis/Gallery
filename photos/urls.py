from django.conf.urls import url, include
from . import views

app_name = 'photos'

urlpatterns = [
    url('^$', views.index, name='index')
]