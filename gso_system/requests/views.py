from django.shortcuts import render

# Create your views here.
def accomplishment_report(request):
    return render(request, 'accomplishment_report/accomplishment_report.html')