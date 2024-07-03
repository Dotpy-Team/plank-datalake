from django.db import models
from .raci import RaciActivity
from .system import System

class DataSet(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    str_status = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
        ]
    )

    raci_activity = models.ForeignKey(
        RaciActivity, 
        on_delete=models.CASCADE,
        related_name='owner',
        null=True, 
        blank=True
    )

    str_title = models.CharField(max_length=200, null=True, blank=True)
    str_desc = models.CharField(max_length=200, null=True, blank=True)
    str_desc_ia = models.CharField(max_length=200, null=True, blank=True)
    dth_start_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.str_title