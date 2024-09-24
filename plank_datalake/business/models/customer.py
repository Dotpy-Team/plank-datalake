from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    str_aws_account_id = models.CharField(max_length=25, null=True, blank=True)
    str_aws_access_key_id = models.CharField(max_length=50, null=True, blank=True)
    str_aws_secret_key = models.CharField(max_length=80, null=True, blank=True)
    str_aws_region = models.CharField(
        max_length=30,
        default= 'us-east-1',
        choices=[
            ('us-east-1', 'US East (N. Virginia)'),
            ('us-east-2 ', 'US East (Ohio)'),
            ('us-west-1', 'US West (N. California)'),
            ('us-west-2', 'US West (Oregon)'),
            ('ca-central-1', 'Canada (Central)'),
            ('sa-east-1', 'South America (São Paulo)'),
            ('eu-north-1 ', 'Europe (Stockholm)'),
            ('eu-west-1', 'Europe (Ireland)'),
            ('eu-west-2', 'Europe (London)'),
            ('eu-west-3', 'Europe (Paris)'),
            ('eu-central-1', 'Europe (Frankfurt)'),
            ('eu-south-1', 'Europe (Milan)'),
            ('eu-south-2', 'Europe (Spain)')
        ])
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
        max_length=20, 
        choices=[
            ('TECH', 'Tecnologia'),
            ('ADM', 'Administrativo'), 
            ('JUR', 'Jurídico'),
            ('FIN', 'Financeiro'),
            ('SAU', 'Saúde'),
            ('EDU', 'Educação'),
            ('COM', 'Comunicação'),
            ('ART', 'Arte e Cultura'),
            ('AGR', 'Agrícola'),
            ('IND', 'Industrial'),
            ('ALI', 'Alimentício'),
            ('AUT', 'Automotivo'),
            ('CON', 'Construção'),
            ('SER', 'Serviços'),
            ('PET', 'Petróleo e Gás'),
            ('MEI', 'Microempreendedor Individual'),
            ('OUT', 'Outros')
        ]
    )
    str_size = models.CharField(
        max_length=20, 
        choices=[
            ('PEQ', 'Pequena'),
            ('PEQ_MEDIA', 'Pequena/Média'), 
            ('MEDIA', 'Média'),
            ('MEDIA_GRANDE', 'Média/Grande'),
            ('GRANDE', 'Grande')
        ]
    )
    dth_create = models.DateField()
    dth_start_at = models.DateField(auto_now=True)
    str_finance_complement = models.CharField(max_length=500)
    str_documents = models.CharField(max_length=200, null=True, blank=True)
    str_comments = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.str_name
