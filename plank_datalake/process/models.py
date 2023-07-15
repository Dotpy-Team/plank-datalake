from django.db import models

class Tables(models.Model):
    """
    Model that represents a table in the metadata table.

    Fields:
        id_table (AutoField): Unique identifier for each table in the metadata table.
        id_customer (ForeignKey): Foreign key to the associated company.
        id_workload (ForeignKey, optional): Foreign key to the associated workload (if any).
        str_system (CharField): The name of the source system.
        str_frequency (CharField): Frequency of updates (daily, monthly, hourly, weekly).
        int_hour_of (IntegerField): Expected hour of update.
        str_mode (CharField): Mode of update (batch or incremental).
        str_type (CharField): Type of update (cdc or full).
        str_dataset (CharField): The group to which the table belongs.
        str_name (CharField): The name of the table in the database.
        str_desc (TextField): A description of the purpose or content of the table.
        str_owner (CharField): The owner or responsible for the table.
        str_owner_email (EmailField): Email of the table owner.
        dth_start_at (DateField): The date the table was created.
        dth_last_updated (DateTimeField): The date and time of the last update made to the table.
        int_size (IntegerField): Size of the table.
        int_number_of_rows (IntegerField): Number of rows in the table.
        float_perc_growth (FloatField): Percentage growth between ingestions.
        str_id_version (CharField): ID hash of the artifact JSON version.
    """

    id_table = models.AutoField(primary_key=True)
    # id_customer = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    # id_workload = models.ForeignKey('Workload', null=True, blank=True, on_delete=models.CASCADE)
    id_customer = models.IntegerField()
    id_workload = models.IntegerField()
    str_system = models.CharField(max_length=200)
    str_frequency = models.CharField(
        max_length=20, choices=[
            ('daily', 'Daily'), 
            ('monthly', 'Monthly'), 
            ('hourly', 'Hourly'), 
            ('weekly', 'Weekly')
        ]
    )
    int_hour_of = models.IntegerField()
    str_mode = models.CharField(
        max_length=20, 
        choices=[
            ('batch', 'Batch'), 
            ('incremental', 'Incremental')
        ]
    )
    str_type = models.CharField(
        max_length=20, 
        choices=[
            ('cdc', 'CDC'), 
            ('full', 'Full')
        ]
    )
    str_dataset = models.CharField(max_length=200)
    str_name = models.CharField(max_length=200)
    str_desc = models.TextField()
    str_owner = models.CharField(max_length=200)
    str_owner_email = models.EmailField()
    dth_start_at = models.DateField(auto_now=True)
    dth_last_updated = models.DateTimeField()
    int_size = models.IntegerField()
    int_number_of_rows = models.IntegerField()
    float_perc_growth = models.FloatField()
    str_id_version = models.CharField(max_length=200)