from django.db import models 
from business.models import Customer 
from process.models import Tables 


class Pipeline(models.Model): 
    pipeline_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dth_start_at = models.DateTimeField()
    dth_end_at = models.DateTimeField()
    str_title = models.CharField(max_length=80)
    str_desc = models.TextField()

    def __str__(self):
        return self.str_title
