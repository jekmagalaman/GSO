from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def requestor_request_management(request):
    return render(request, 'requestor_request_management/requestor_request_management.html') 



