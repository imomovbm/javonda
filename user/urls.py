from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'), 
]
