from django.urls import path
from . import views

urlpatterns = [
    path('', views.personnel_task_management, name='personnel-dashboard'),
    path('personnel-task-management/', views.personnel_task_management, name='personnel_task_management'),
    path('personnel-inventory/', views.personnel_inventory, name='personnel_inventory'),
    path('personnel-history/', views.personnel_history, name='personnel_history'),
]