# crawler/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('crawler/', index, name='index')
]
