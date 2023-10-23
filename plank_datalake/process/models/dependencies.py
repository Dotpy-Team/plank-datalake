from django.db import models
from business.models import DataSet, Customer

class Dependencies(models.Model):

    id_dependencie = models.AutoField(primary_key=True)
    id_table_node = models.IntegerField()
    id_table_edge = models.IntegerField()
    str_status = models.CharField(max_length=200)
    dth_start_at = models.DateTimeField()
    dth_last_update = models.DateTimeField()