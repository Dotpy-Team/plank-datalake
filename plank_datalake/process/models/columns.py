from django.db import models
from business.models import Customer
from .tables import Tables

class Columns(models.Model):

    id_column = models.AutoField(primary_key=True)
    #TODO: colocar campo como forenkey esta como numerico para teste.
    table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    str_source_name = models.CharField(max_length=60)
    str_rename = models.CharField(max_length=60)
    str_datatype = models.CharField(
        max_length=60,
        choices=[
            ('string', 'String'),
            ('int', 'Integer'),
            ('bigint', 'BigInt'),
            ('double', 'Float'),
            ('timestamp', 'Date'),
            ('timestamp', 'Datetime')
        ]
    )
    str_pattern_format = models.CharField(max_length=60)
    str_type = models.CharField(
        max_length=20,
        choices=[
            ('CPK', 'Chave Primaria.'),
            ('CFK', 'Chave Extrangeira.'),
            ('KDS', 'Campo Descritivo.'),
            ('SEN','Dados Sensiveis')
        ]
    )

    str_desc = models.CharField(max_length=60)