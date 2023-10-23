from django.db import models
from .contract import Contract
from .service import Service

class ContractItem(models.Model):
    id_contractitem = models.AutoField(primary_key=True)
    id_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    id_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    dth_created_at = models.DateField(auto_now=True)
    dth_updated_at = models.DateField(auto_now=True)