from django.db import models

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    str_title = models.CharField(max_length=200, null=True, blank=True)
    str_descr = models.CharField(max_length=200, null=True, blank=True)
    int_price = models.IntegerField(null=True, blank=True)
    int_qnt = models.IntegerField(null=True, blank=True)
    str_status = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
        ]
    )
    dth_created_at = models.DateField(auto_now=True)
    dth_updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.str_title