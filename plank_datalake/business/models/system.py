from django.db import models
from .customer import Customer

class System(models.Model):
    system_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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
    table_type = models.CharField(max_length=50)

    #Google Sheets
    type = models.CharField(max_length=80, blank=True, null=True)
    project_id = models.CharField(max_length=80, blank=True, null=True)
    private_key_id = models.CharField(max_length=100, blank=True, null=True)
    private_key = models.TextField(blank=True, null=True)
    client_email = models.CharField(max_length=100, blank=True, null=True)
    client_id = models.CharField(max_length=80, blank=True, null=True)
    auth_uri = models.CharField(max_length=80, blank=True, null=True)
    token_uri = models.CharField(max_length=80, blank=True, null=True)
    auth_provider_x509_cert_url = models.CharField(max_length=80, blank=True, null=True)
    client_x509_cert_url = models.CharField(max_length=200, blank=True, null=True)
    universe_domain = models.CharField(max_length=50, blank=True, null=True)

    #PostGree
    engine = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    user = models.CharField(max_length=80, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(max_length=80, blank=True, null=True)
    port = models.CharField(max_length=80, blank=True, null=True)

    #MySQL
    passwd = models.CharField(max_length=50, blank=True, null=True)
    database = models.CharField(max_length=80, blank=True, null=True)

    #SQLite
    database_name = models.CharField(max_length=50, blank=True, null=True)