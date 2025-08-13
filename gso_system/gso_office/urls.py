from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_management, name='gso-dashboard'),
    path('accomplishment-report/', views.accomplishment_report, name='accomplishment_report'),
    path('gso-inventory/', views.gso_inventory, name='gso_inventory'),
    path('account-management/', views.account_management, name='account_management'),

    path('gso/', views.request_management, name='request_management'),

    path('accounts/', views.account_view, name='account_management'),

    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),

]
