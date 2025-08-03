from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def unit_head_dashboard(request):
    return render(request, 'unit_head_dashboard/unit_head_dashboard.html')  # make sure this template exists

def unit_head_inventory(request):
    return render(request, 'unit_head_inventory/unit_head_inventory.html')

def unit_head_request_history(request):
    return render(request, 'unit_head_request_history/unit_head_request_history.html')