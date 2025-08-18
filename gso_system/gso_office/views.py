from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from .forms import UserEditForm




# Optional: check if user is GSO role
def is_gso(user):
    return user.is_authenticated and user.role == 'gso'  # adjust based on your custom User model

@login_required
@user_passes_test(is_gso)  # optional, only allow GSO users

def request_management(request):
    context = {
        'user_role': request.user.role  
    }
    return render(request, 'request_management/request_management.html')

def accomplishment_report(request):
    return render(request, 'accomplishment_report/accomplishment_report.html')

def gso_inventory(request):
    return render(request, 'inventory/gso_inventory.html')

def account_management(request):
    return render(request, 'accounts/account_management.html')




User = get_user_model()

def account_view(request):
    users = User.objects.all()
    return render(request, 'accounts/account_management.html', {'users': users})


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account_management')  # Go back to the list
    else:
        form = UserEditForm(instance=user)
    
    return render(request, 'accounts/account_edit.html', {'form': form, 'user': user})





