from django.db import models
from business.models import Customer


class Conector(models.Model):
    conector_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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

    engine = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    user = models.CharField(max_length=80, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(max_length=80, blank=True, null=True)
    port = models.CharField(max_length=80, blank=True, null=True)
    

    def __str__(self):
        return self.project_id + self.name
        