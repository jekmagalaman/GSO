from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Optional: check if user is GSO role
def is_gso(user):
    return user.is_authenticated and user.role == 'gso'  # adjust based on your custom User model

@login_required
@user_passes_test(is_gso)  # optional, only allow GSO users




def gso_dashboard(request):
    context = {
        'user_role': request.user.role  # OR request.user.profile.role depending on your model
    }
    return render(request, 'dashboard/gso_dashboard.html')

def accomplishment_report(request):
    return render(request, 'accomplishment_report/accomplishment_report.html')

def employee_management(request):
    return render(request, 'employee/employee_management.html')

def account_management(request):
    return render(request, 'accounts/account_management.html')