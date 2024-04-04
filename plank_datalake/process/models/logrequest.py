from django.db import models
from business.models import Customer


class LogRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    str_url = models.CharField(max_length=200)
    str_method = models.CharField(max_length=80)
    str_request_body = models.TextField()
    str_response_status = models.IntegerField()
    str_response_body = models.TextField()
