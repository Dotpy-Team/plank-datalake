from django.db import models

class ModelTest(models.Model):
    id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=30)