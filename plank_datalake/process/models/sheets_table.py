from django.db import models 


class SheetsTable(models.Model):
    id_sheet = models.AutoField(primary_key=True)
    type = models.CharField(max_length=80)
    project_id = models.CharField(max_length=80)
    private_key_id = models.CharField(max_length=100)
    private_key = models.TextField()
    client_email = models.CharField(max_length=100)
    client_id = models.CharField(max_length=80)
    auth_uri = models.CharField(max_length=80)
    token_uri = models.CharField(max_length=80)
    auth_provider_x509_cert_url = models.CharField(max_length=80)
    client_x509_cert_url = models.CharField(max_length=200)
    universe_domain = models.CharField(max_length=50)
