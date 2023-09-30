from django.db import models

class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    id_customer = models.IntegerField(null=True, blank=True)
    id_table = models.IntegerField(null=True, blank=True)
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
