from django.db import models 
from business.models import Customer


class Trigger(models.Model):
    trigger_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    str_cron = models.TextField()
    str_title = models.CharField(max_length=80)
    str_status = models.CharField(max_length=21)

    def __str__(self):
        return self.str_title
