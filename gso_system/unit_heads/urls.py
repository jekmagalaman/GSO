from django.urls import path
from . import views

urlpatterns = [
    path('', views.unit_head_request_management, name='unit-head-dashboard'),
    path('unit-head-request-management/', views.unit_head_request_management, name='unit_head_request_management'),
    path('unit-head-inventory/', views.unit_head_inventory, name='unit_head_inventory'),
    path('unit-head-request_history/', views.unit_head_request_history, name='unit_head_request_history'),
]
