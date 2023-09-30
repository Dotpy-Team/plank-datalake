from django.db import models

class ConfCluster(models.Model):
    #configure to start_job_run
    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_job_run.html
    id_cluster = models.AutoField(primary_key=True)
    str_worker_type = models.CharField(max_length=200, null=True, blank=True)
    str_numer_of_workers = models.CharField(max_length=200, null=True, blank=True)
    int_time_out = models.IntegerField()
    int_max_capacity = models.IntegerField()
    str_status = models.CharField(
        max_length=20, choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
        ]
    )