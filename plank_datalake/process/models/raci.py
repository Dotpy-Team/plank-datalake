from django.db import models
from business.models import Customer, CustomUser

class RaciActivity(models.Model):
    #vai armazenar os processos
    activity_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    str_title = models.CharField(max_length=200)
    str_desc = models.CharField(max_length=200)
    dth_created_at = models.DateTimeField(auto_now_add=True)
    responsible = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='responsible')
    accountable = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='accountable')

    str_shareable = models.CharField(
        max_length=30,
        choices=(
            ('True', 'True'),
            ('False', 'False')
        )
    )

    str_color = models.CharField(
        max_length=30,
        choices=(
            ('red', 'red'),
            ('green', 'green'),
            ('blue', 'blue')
        )
    )
    
    def __str__(self):
        return self.str_title


class RaciRelated(models.Model):
    #vai armazenar o relacionamento entre usuario e a role.
    related_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    activity = models.ForeignKey(RaciActivity, on_delete=models.CASCADE)
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='person')
    dth_add = models.DateTimeField(auto_now_add=True)
    str_type = models.CharField(
        max_length=20, choices=[
            ('CON','Consultado'),
            ('INF','Informado')
        ]
    )

