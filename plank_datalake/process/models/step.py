from django.db import models 
from business.models import Customer 
from process.models import Tables, Pipeline


class Step(models.Model): 
    step_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    # table = models.IntegerField()
    str_query = models.TextField()
