from django.conf.urls import url
from . import views

app_name = 'photos'

urlpatterns = [
    url(r'^photos/', views.index, name='index')
]