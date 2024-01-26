from django.db import models
from business.models import DataSet, Customer
from .raci import RaciActivity
from .step import Step


class Tables(models.Model):
    table_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE, null=True, blank=True)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, null=True, blank=True)
    layer = models.CharField(max_length=20)
    str_frequency = models.CharField(
        max_length=20, choices=[
            ('Daily', 'Diario'), 
            ('Montly', 'Mensal'), 
            ('Hour', 'A cada 1 hora'), 
            ('Weekly', 'Semanal')
        ],
        null=True, 
        blank=True
    )

    str_type_of = models.CharField(
        max_length=20, 
        choices=[
            ('Procedure', 'Procedure'), 
            ('Ingestion', 'Ingestion'), 
            ('Copy', 'Copy')
        ],
        null=True,
        blank=True
    )

    str_mode = models.CharField(
        max_length=20, 
        choices=[
            ('Batch', 'Batch'), 
            ('Incremental', 'Incremental')
        ],
        null=True,
        blank=True
    )

    str_type = models.CharField(
        max_length=20, 
        choices=[
            ('CDC', 'Detecte as Mudanças'),
            ('FULL', 'Considere a Ultima Particao')
        ],
        null=True,
        blank=True
    )

    str_name = models.CharField(max_length=200)
    str_desc = models.TextField()
    str_desc_ia = models.TextField()

    raci_activity = models.ForeignKey(
        RaciActivity, 
        on_delete=models.CASCADE,
        related_name='owner',
        null=True, 
        blank=True
    )

    dth_start_at = models.DateTimeField(auto_now=True)
    dth_last_updated = models.DateTimeField(null=True, blank=True)
    
    int_size = models.IntegerField(null=True, blank=True)
    int_number_of_rows = models.IntegerField(null=True, blank=True)
    float_perc_growth = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.str_name
