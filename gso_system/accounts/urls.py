from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('redirect/', views.role_redirect, name='role-redirect'),

    path('employee-management/', views.employee_management, name='employee_management'),

    path('account-management/', views.account_management, name='account_management'),
]
