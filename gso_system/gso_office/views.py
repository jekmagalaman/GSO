from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Optional: check if user is GSO role
def is_gso(user):
    return user.is_authenticated and user.role == 'gso'  # adjust based on your custom User model

@login_required
@user_passes_test(is_gso)  # optional, only allow GSO users
def gso_dashboard(request):
    return render(request, 'dashboard/gso_dashboard.html')
