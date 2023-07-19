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

class Columns(models.Model):
    """
       Model Columns represent where the columns of table is storaged metadados.

        Fields: 

            id_column (Autofield): Unique identifier for each workload in the procedures.
            id_table (ForeignKey): Foreign key to the associated company.
            str_source_name (CharField): Name of column in the source.
            str_rename (CharField): Name of column after is renamed in datalake.
            str_from_datatype (CharField): datatype befour transform.
            str_datatype_to_apply (CharField): datatype after transform and apply casting in datalake.
            str_pattern_format (CharField): pattern to transform value in datacleasing datalake.

            str_primary_key = models.IntegerField()
            str_change_data_capture = models.IntegerField()

            str_desc (CharField): Description of the column content.
    """

    id_column = models.AutoField(primary_key=True)
    # id_table = models.ForeignKey(Tables, on_delete=models.CASCADE)
    id_table = models.IntegerField()
    str_source_name = models.CharField(max_length=60)
    str_rename = models.CharField(max_length=60)
    str_from_datatype = models.CharField(max_length=60)
    str_datatype_to_apply = models.CharField(max_length=60)
    str_pattern_format = models.CharField(max_length=60)
    str_primary_key = models.IntegerField()
    str_change_data_capture = models.IntegerField()
    str_desc = models.CharField(max_length=60)


class WorkLoads(models.Model):
    """
        Model workload represent where the procedures of company is storage to run when is called.

        Fields:

            id_workload (Autofield): Unique identifier for each workload in the procedures.
            id_customer (ForeignKey): Foreign key to the associated company.
            id_table (ForeignKey): Foreign key to the associated table.
            str_project (CharField): Project that this procedure is executed.
            str_relative_import (charField): Relative import from python to use in whl.
            dth_start_at (DateField): The date the table was created.
            dth_last_updated (DateTimeField): The date and time of the last update made to the table.
    
    """

    id_workload = models.AutoField(primary_key=True)
    id_customer = models.IntegerField()
    # id_customer = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    # id_workload = models.ForeignKey('Workload', null=True, blank=True, on_delete=models.CASCADE)
    id_table = models.IntegerField()
    str_project = models.CharField(max_length=200)
    str_relative_import = models.CharField(max_length=200)
    dth_last_updated = models.DateTimeField()
    dth_start_at = models.DateTimeField()

class Dependencies(models.Model):
    """
    Model dependencies represent a graph where edge is dependencie from node, node is been run only.
    Define the structure of the graph with nodes and edges.
            Fields:
                id_dependencie = models.AutoField(primary_key=True)
                id_workload_node = models.IntegerField()
                id_workload_edge = models.IntegerField()
                str_status = models.CharField(max_length=200)
                dth_start_at = models.DateTimeField()

    """

    id_dependencie = models.AutoField(primary_key=True)
    id_workload_node = models.IntegerField()
    id_workload_edge = models.IntegerField()
    str_status = models.CharField(max_length=200)
    dth_start_at = models.DateTimeField()


class JobRun(models.Model):
    """
    
    Model jobRun represent where the procedures or ingestion is storaged where is processed.

        Fields:

            id_workload (Autofield): Unique identifier for each workload in the procedures.
            dth_start_at (DateField): The date the table was created.
            dth_last_updated (DateTimeField): The date and time of the last update made to the table.
            str_status (charField): if is sucecceded or failled.
    
    """

    id_job = models.AutoField(primary_key=True)
    id_workload = models.IntegerField()
    dth_last_updated = models.DateTimeField()
    dth_start_at = models.DateTimeField()
    int_total_size = models.IntegerField()
    int_total_rows = models.IntegerField()