from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def personnel_task_management(request):
    return render(request, 'personnel_task_management/personnel_task_management.html')

def personnel_inventory(request):
    return render(request, 'personnel_inventory/personnel_inventory.html')

def personnel_history(request):
    return render(request, 'personnel_history/personnel_history.html')

