from django.db import models

class Tables(models.Model):

    id_table = models.AutoField(primary_key=True)
    #TODO: adicionar os campos como forenkey (esta como numérico para teste)
    # id_customer = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    # id_workload = models.ForeignKey('Workload', null=True, blank=True, on_delete=models.CASCADE)
    id_customer = models.IntegerField()
    str_system = models.CharField(max_length=200)
    str_frequency = models.CharField(
        max_length=20, choices=[
            ('Daily', 'Diario'), 
            ('Montly', 'Mensal'), 
            ('Hour', 'A cada 1 hora'), 
            ('Weekly', 'Semanal')
        ],
        null=True, 
        blank=True
    )

    str_project = models.CharField(max_length=200, null=True, blank=True)
    str_event_bridge = models.CharField(max_length=200, null=True, blank=True)

    str_relative_import = models.CharField(max_length=200)
    str_type_of = models.CharField(
        max_length=20, 
        choices=[
            ('Procedure', 'Procedure'), 
            ('Ingestion', 'Ingestion'), 
            ('Copy', 'Copy')
        ]
    )

    str_hour_of = models.CharField(max_length=200, null=True, blank=True)

    str_mode = models.CharField(
        max_length=20, 
        choices=[
            ('Batch', 'Batch'), 
            ('Incremental', 'Incremental')
        ]
    )

    str_type = models.CharField(
        max_length=20, 
        choices=[
            ('CDC', 'Detecte as Mudanças'),
            ('ULP', 'Considere a Ultima Particao')
        ]
    )

    str_dataset = models.CharField(
            max_length=20, 
            choices=[
                ('CAD', 'Cadastro'),
                ('TRAN', 'Transacional'),
                ('LOG', 'Traking'),
                ('JUD', 'Juridico'),
                ('TECH', 'Tecnologia'),
                ('ADM', 'Administrativo'),
                ('FUP', 'Follow Up'),
                ('IOT', 'Sensores'),
                ('MED', 'Registros Medicos'),
                ('FAT', 'Faturamento')
            ]
        )

    str_name = models.CharField(max_length=200)
    str_desc = models.TextField()
    str_owner = models.CharField(max_length=200)
    str_owner_email = models.EmailField()
    dth_start_at = models.DateTimeField(auto_now=True)
    dth_last_updated = models.DateTimeField(null=True, blank=True)
    int_size = models.IntegerField(null=True, blank=True)
    int_number_of_rows = models.IntegerField(null=True, blank=True)
    float_perc_growth = models.FloatField(null=True, blank=True)
    str_id_version = models.CharField(max_length=200, null=True, blank=True)

class Columns(models.Model):

    id_column = models.AutoField(primary_key=True)
    #TODO: colocar campo como forenkey esta como numerico para teste.
    # id_table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    id_table = models.IntegerField()
    str_source_name = models.CharField(max_length=60)
    str_rename = models.CharField(max_length=60)
    str_datatype = models.CharField(max_length=60)
    str_pattern_format = models.CharField(max_length=60)
    str_type = models.CharField(
        max_length=20,
        choices=[
            ('PK', 'Detecte as Mudanças'), 
            ('CDC', 'Ultima fotografia'), 
            ('NA', 'Nao Aplicavel')
        ]
    )

    str_desc = models.CharField(max_length=60)


class Dependencies(models.Model):

    id_dependencie = models.AutoField(primary_key=True)
    id_table_node = models.IntegerField()
    id_table_edge = models.IntegerField()
    str_status = models.CharField(max_length=200)
    dth_start_at = models.DateTimeField()
    dth_last_update = models.DateTimeField()


class JobRun(models.Model):

    id_job = models.CharField(max_length=200)
    id_table = models.IntegerField()
    dth_last_updated = models.DateTimeField()
    dth_start_at = models.DateTimeField()
    str_status = models.CharField(max_length=200)
    int_total_size = models.IntegerField()
    int_total_rows = models.IntegerField()