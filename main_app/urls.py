
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('label/',views.label,name='label'),
]