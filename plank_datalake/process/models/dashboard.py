from django.db import models 
from business.models import Customer 
from .raci import RaciActivity


class Dashboard(models.Model): 
    dashboard_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    raci_activity = models.ForeignKey(RaciActivity, on_delete=models.CASCADE)
    dth_start_at = models.DateTimeField()
    str_title = models.CharField(max_length=80)
    str_desc = models.TextField()

    def __str__(self):
        return self.str_title

# class DashboardSlide(models.Model):
#     slide_id = models.AutoField(primary_key=True)
#     dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
#     dynamodbkey = models.CharField(max_length=80)
#     str_title = models.CharField(max_length=80)
#     str_desc = models.TextField()

#     def __str__(self):
#         return self.str_title