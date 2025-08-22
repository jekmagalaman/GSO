from django.urls import path
from . import views

urlpatterns = [
    path('', views.requestor_request_management, name='employee-dashboard'),
    path('requestor-request-management/', views.requestor_request_management, name='requestor_request_management'),
    
]
