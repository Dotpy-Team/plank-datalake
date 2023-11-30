from django.db import models
from .contract import Contract
from .service import Service

class ContractItem(models.Model):
    contractitem_id = models.AutoField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    dth_created_at = models.DateField(auto_now=True)
    dth_updated_at = models.DateField(auto_now=True)