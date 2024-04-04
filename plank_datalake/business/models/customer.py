from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    str_customer_type = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo'), 
            ('Prospec', 'Prospec'),
            ('Teste', 'Teste'),
            ('Admin', 'Admin')
        ]
    )
    str_name = models.CharField(max_length=200, null=True, blank=True)
    str_cnpj = models.CharField(max_length=200, null=True, blank=True)
    str_address = models.CharField(max_length=200, null=True, blank=True)
    str_telefone = models.CharField(max_length=200, null=True, blank=True)
    str_email = models.CharField(max_length=200)
    str_site = models.CharField(max_length=200)
    str_linkedin_profile = models.CharField(max_length=200, null=True, blank=True)
    str_contact = models.CharField(max_length=200, null=True, blank=True)
    str_setor = models.CharField(
        max_length=20, choices=[
            ('TECH', 'TECH'),
            ('ADM', 'ADM'), 
            ('JUR', 'JUR'),
            ('FIN', 'FIN'),
            ('LOG', 'LOG')
        ]
    )
    str_size = models.CharField(
        max_length=20, choices=[
            ('PEQ', 'PEQ'),
            ('PEQ MEDIA', 'PEQ MEDIA'), 
            ('MEDIA', 'MEDIA'),
            ('MEDIA GRANDE', 'MEDIA GRANDE'),
            ('GRANDE', 'GRANDE')
        ]
    )
    dth_create = models.DateField()
    dth_start_at = models.DateField(auto_now=True)
    str_finance_complement = models.CharField(max_length=500)
    str_documents = models.CharField(max_length=200, null=True, blank=True)
    str_comments = models.CharField(max_length=200, null=True, blank=True)
    str_cod_aws_account = models.CharField(max_length=200)

    def __str__(self):
        return self.str_name
