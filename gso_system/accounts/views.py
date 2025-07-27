from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def role_redirect(request):
    user = request.user
    if user.role == 'gso':
        return redirect('gso-dashboard')
    elif user.role == 'unit_head':
        return redirect('unit-head-dashboard')
    elif user.role == 'personnel':
        return redirect('personnel-dashboard')
    elif user.role == 'employee':
        return redirect('employee-dashboard')
    else:
        return redirect('login')


def employee_management(request):
    return render(request, 'employee/employee_management.html')

def account_management(request):
    return render(request, 'accounts/account_management.html')