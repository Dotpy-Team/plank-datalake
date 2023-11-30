from django.db import models
from .customer import Customer

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.IntegerField(null=True, blank=True)
    str_title = models.CharField(max_length=200, null=True, blank=True)
    str_desc = models.CharField(max_length=200, null=True, blank=True)
    str_documents = models.CharField(max_length=200, null=True, blank=True)
    str_status = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
        ]
    )
    dth_create = models.DateField(auto_now=True)
    dth_start_at = models.DateField()
    dth_end_at = models.DateField()
