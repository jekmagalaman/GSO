from django.urls import path
from . import views

urlpatterns = [
    path('', views.unit_head_dashboard, name='unit-head-dashboard'),
    path('unit-head-dashboard/', views.unit_head_dashboard, name='unit_head_dashboard'),
    path('unit-head-inventory/', views.unit_head_inventory, name='unit_head_inventory'),
    path('unit-head-request_history/', views.unit_head_request_history, name='unit_head_request_history'),
]
