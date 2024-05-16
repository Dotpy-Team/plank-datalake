from django.db import models 
from business.models import Customer 

class Contacts(models.Model): 
    contact_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    str_first_name = models.CharField(max_length=80)
    str_last_name = models.CharField(max_length=80)
    str_email = models.CharField(max_length=80)
    str_comercial_email = models.CharField(max_length=80)
    str_phone_number = models.CharField(max_length=20)
    str_comercial_phone_number = models.CharField(max_length=20)
    str_whatspp_number = models.CharField(max_length=20)
    str_type_contact = models.CharField(
        max_length=30,
        choices=[
            ('Admin', 'Admin'),
            ('Employee', 'Employee')
        ]
    )

    def __str__(self):
        return self.str_email