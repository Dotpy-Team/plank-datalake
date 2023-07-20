from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    """
    classe utilizada para criar usuários no sistema, viculados a alguma empresa.

    """

    str_cpf = models.CharField(
        max_length=14, 
        # unique=True, 
        null=True, 
        blank=True
    )
    
    id_company = models.IntegerField()
    
    str_telefone = models.CharField(
        max_length=15, 
        null=True, 
        blank=True
    )

    str_cargo = models.CharField(
        max_length=100,
        null=True, 
        blank=True
    )
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    def __str__(self):
        return self.username
    
class Customer(models.Model):
    """
    classe utilizada para armazenar clientes em prospecção ou clientes usuários do sistema.
    
    """
    id_customer = models.AutoField(primary_key=True)
    id_customer_type = models.CharField(
        max_length=20, choices=[
            ('cliente_ativo', 'cliente_ativo'),
            ('cliente_inativo', 'cliente_inativo'), 
            ('prospeccao', 'prospeccao'),
            ('teste', 'teste'),
            ('adm', 'adm')
        ]
    )
    str_name = models.CharField(max_length=200)
    str_cnpj = models.CharField(max_length=200)
    str_address = models.CharField(max_length=200)
    str_telefone = models.CharField(max_length=200)
    str_email = models.CharField(max_length=200)
    str_site = models.CharField(max_length=200)
    str_linkedin_profile = models.CharField(max_length=200)
    str_contact = models.CharField(max_length=200)
    str_setor = models.CharField(max_length=200)
    str_size = models.CharField(max_length=200)
    dth_create = models.DateField()
    dth_start_at = models.DateField(auto_now=True) 
    str_finance_complement = models.CharField(max_length=500)
    str_documents = models.CharField(max_length=200)
    str_comments = models.CharField(max_length=200)