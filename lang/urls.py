from . import views
from django.urls import path

app_name = 'lang'

urlpatterns=[
    path('', views.home, name='home'),
]