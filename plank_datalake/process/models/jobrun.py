from django.db import models
from business.models import Customer
from .tables import Tables


class JobRun(models.Model):
    job_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    dth_last_updated = models.DateTimeField()
    dth_start_at = models.DateTimeField()
    str_status = models.CharField(max_length=200)
    int_total_size = models.IntegerField()
    int_total_rows = models.IntegerField()
    str_event_bucket_trigger = models.CharField(max_length=100)
    str_event_key_trigger = models.CharField(max_length=100)
