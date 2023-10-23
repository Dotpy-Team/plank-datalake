from django.db import models
from .customer import Customer

class Contract(models.Model):
    id_contract = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    str_title = models.CharField(max_length=200, null=True, blank=True)
    str_object = models.CharField(max_length=200, null=True, blank=True)
    str_status = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
        ]
    )

    dth_created_at = models.DateField(auto_now=True)
    dth_start_at = models.DateField()
    dth_end_at = models.DateField()
    dth_updated_at = models.DateField(auto_now=True)

