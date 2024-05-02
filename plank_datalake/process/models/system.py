from django.db import models
from business.models import Customer

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
    str_table_type = models.CharField(max_length=50)

    #Google Sheets
    str_type = models.CharField(max_length=80, blank=True, null=True)
    str_project_id = models.CharField(max_length=80, blank=True, null=True)
    str_private_key_id = models.CharField(max_length=100, blank=True, null=True)
    str_private_key = models.TextField(blank=True, null=True)
    str_client_email = models.CharField(max_length=100, blank=True, null=True)
    str_client_id = models.CharField(max_length=80, blank=True, null=True)
    str_auth_uri = models.CharField(max_length=80, blank=True, null=True)
    str_token_uri = models.CharField(max_length=80, blank=True, null=True)
    str_auth_provider_x509_cert_url = models.CharField(max_length=80, blank=True, null=True)
    str_client_x509_cert_url = models.CharField(max_length=200, blank=True, null=True)
    str_universe_domain = models.CharField(max_length=50, blank=True, null=True)

    #PostGree
    str_engine = models.CharField(max_length=100, blank=True, null=True)
    str_name = models.CharField(max_length=80, blank=True, null=True)
    str_user = models.CharField(max_length=80, blank=True, null=True)
    str_password = models.CharField(max_length=50, blank=True, null=True)
    str_host = models.CharField(max_length=80, blank=True, null=True)
    str_port = models.CharField(max_length=80, blank=True, null=True)

    #MySQL
    str_passwd = models.CharField(max_length=50, blank=True, null=True)
    str_database = models.CharField(max_length=80, blank=True, null=True)

    #SQLite
    str_database_name = models.CharField(max_length=50, blank=True, null=True)