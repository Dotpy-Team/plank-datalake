from django.db import models
from business.models import DataSet, Customer
from process.models import Tables

class Dependencies(models.Model):

    dependencie_id = models.AutoField(primary_key=True)
    table_node = models.ForeignKey(Tables, on_delete=models.CASCADE)
    # table_edge = models.ForeignKey(Tables, on_delete=models.CASCADE)
    str_status = models.CharField(max_length=200)
    dth_start_at = models.DateTimeField()
    dth_last_update = models.DateTimeField()