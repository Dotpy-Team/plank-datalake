from django.db import models

class DataSet(models.Model):
    id_dataset = models.AutoField(primary_key=True)
    id_system = models.IntegerField()
    str_status = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
        ]
    )
    str_title = models.CharField(max_length=200, null=True, blank=True)
    str_desc = models.CharField(max_length=200, null=True, blank=True)
    str_desc_ia = models.CharField(max_length=200, null=True, blank=True)
    dth_start_at = models.DateField(auto_now=True)
