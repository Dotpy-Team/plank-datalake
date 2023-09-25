from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('O usuário deve ser fornecido')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O superusuário deve ter is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    str_cpf = models.CharField(max_length=14, null=True, blank=True) #TODO: adicionar o cpf como unico. unique=True,)
    id_customer = models.IntegerField()
    str_telefone = models.CharField(max_length=15, null=True, blank=True)
    str_cargo = models.CharField(max_length=100, null=True, blank=True)
    str_address = models.CharField(max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='custom_users')    
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Customer(models.Model):

    id_customer = models.AutoField(primary_key=True)
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