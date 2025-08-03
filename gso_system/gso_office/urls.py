from django.urls import path
from . import views

urlpatterns = [
    path('', views.gso_dashboard, name='gso-dashboard'),
    path('accomplishment-report/', views.accomplishment_report, name='accomplishment_report'),
    path('employee-management/', views.employee_management, name='employee_management'),
    path('account-management/', views.account_management, name='account_management'),

    path('gso/', views.gso_dashboard, name='gso_dashboard'),

]
