from django.db import models
from requests.models import ServiceRequest

class WorkReport(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    report_text = models.TextField()  # This can be generated using GPT/NLG
    generated_at = models.DateTimeField(auto_now_add=True)
