from django.urls import path
from . import views

urlpatterns = [
    path('', views.gso_dashboard, name='gso_dashboard'),
]
