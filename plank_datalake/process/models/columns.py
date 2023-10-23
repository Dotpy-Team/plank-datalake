from django.db import models
from business.models import DataSet, Customer

class Columns(models.Model):

    id_column = models.AutoField(primary_key=True)
    #TODO: colocar campo como forenkey esta como numerico para teste.
    # id_table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    id_table = models.IntegerField()
    str_source_name = models.CharField(max_length=60)
    str_rename = models.CharField(max_length=60)
    str_datatype = models.CharField(max_length=60)
    str_pattern_format = models.CharField(max_length=60)
    str_type = models.CharField(
        max_length=20,
        choices=[
            ('PK', 'Detecte as Mudanças'), 
            ('CDC', 'Ultima fotografia'), 
            ('NA', 'Nao Aplicavel')
        ]
    )

    str_desc = models.CharField(max_length=60)