from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model


@login_required
def accomplishment_report(request):
    return render(request, 'gso_office/accomplishment_report/accomplishment_report.html')