# requests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #GSO Office URLs
    path('', views.request_management, name='gso-dashboard'),
    path('gso/', views.request_management, name='request_management'),


    #Unit Head URLs
    path('', views.unit_head_request_management, name='unit-head-dashboard'),
    path('unit-head-request-management/', views.unit_head_request_management, name='unit_head_request_management'),
    path('unit-head-request_history/', views.unit_head_request_history, name='unit_head_request_history'),

]
