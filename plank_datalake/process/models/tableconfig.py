from django.db import models
from business.models import Customer


class Conector(models.Model):
    id_conector = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.project_id
        