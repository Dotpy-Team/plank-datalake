from django.db import models
from business.models import  Customer
from .tables import Tables

class Dependencies(models.Model):

    dependency_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table_node = models.ForeignKey(Tables, on_delete=models.CASCADE, related_name='table_node')
    table_edge = models.ForeignKey(Tables, on_delete=models.CASCADE, related_name='table_edge')
