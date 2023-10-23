from django.db import models
from business.models import DataSet, Customer

class Tables(models.Model):
    id_table = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id_dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)
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
        ]
    )

    str_mode = models.CharField(
        max_length=20, 
        choices=[
            ('Batch', 'Batch'), 
            ('Incremental', 'Incremental')
        ]
    )

    str_type = models.CharField(
        max_length=20, 
        choices=[
            ('CDC', 'Detecte as Mudanças'),
            ('FULL', 'Considere a Ultima Particao')
        ]
    )

    str_name = models.CharField(max_length=200)
    str_desc = models.TextField()
    str_desc_ia = models.TextField()

    str_owner_name = models.CharField(max_length=200)
    str_owner_email = models.EmailField()

    dth_start_at = models.DateTimeField(auto_now=True)
    dth_last_updated = models.DateTimeField(null=True, blank=True)
    
    int_size = models.IntegerField(null=True, blank=True)
    int_number_of_rows = models.IntegerField(null=True, blank=True)
    float_perc_growth = models.FloatField(null=True, blank=True)
