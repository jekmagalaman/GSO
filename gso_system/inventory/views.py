from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def gso_inventory(request):
    return render(request, 'gso_office/inventory/gso_inventory.html')


@login_required
def unit_head_inventory(request):
    return render(request, 'unit_heads/unit_head_inventory/unit_head_inventory.html')