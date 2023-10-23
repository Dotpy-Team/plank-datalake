from django.db import models
from business.models import DataSet, Customer

class JobRun(models.Model):

    id_job = models.CharField(max_length=200)
    id_table = models.IntegerField()
    dth_last_updated = models.DateTimeField()
    dth_start_at = models.DateTimeField()
    str_status = models.CharField(max_length=200)
    int_total_size = models.IntegerField()
    int_total_rows = models.IntegerField()