from django.db import models

class Layer(models.Model):
    layer_id = models.AutoField(primary_key=True)
    # customer = models.ForeignKey("app.Model", on_delete=models.CASCADE)
    str_title = models.CharField(max_length=200, null=True, blank=True)
    str_desc = models.CharField(max_length=200, null=True, blank=True)
    str_status = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
        ]
    )