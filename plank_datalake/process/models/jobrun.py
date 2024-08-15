from django.db import models
from business.models import Customer
from .tables import Tables

class JobRun(models.Model):
    job_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    dth_start_at = models.DateTimeField()
    dth_ended_at = models.DateTimeField(null=True, blank=True)
    str_status = models.CharField(
        max_length=20, choices=[
            ('RUNNING', 'RUNNING'),
            ('FAILED', 'FAILED'),
            ('SUCCEEDED', 'SUCCEEDED')
        ],
        null=False,
        default='RUNNING'
    )
    str_event_bucket_trigger = models.CharField(max_length=100, null=True, blank=True)
    str_event_key_trigger = models.CharField(max_length=100, null=True, blank=True)
    str_unique_execution_id = models.CharField(max_length=100,null=True, blank=True)
    str_jr_ingestion_id = models.CharField(max_length=100, null=True, blank=True)
    str_jr_context_id = models.CharField(max_length=100, null=True, blank=True)

class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobRun, on_delete=models.CASCADE)
    dth_event_at = models.DateTimeField()
    str_type = models.CharField(
        max_length=20, choices=[
            ('INFO', 'INFO'),
            ('WARNING', 'WARNING'),
            ('ERROR', 'ERROR')
        ]
    )
    str_desc = models.CharField(max_length=100, null=True, blank=True)    

