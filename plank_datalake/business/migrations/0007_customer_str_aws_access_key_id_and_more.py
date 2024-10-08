# Generated by Django 4.2.6 on 2024-09-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_rename_str_account_id_customer_str_aws_account_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='str_aws_access_key_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='str_aws_region',
            field=models.CharField(choices=[('us-east-1', 'US East (N. Virginia)'), ('us-east-2 ', 'US East (Ohio)'), ('us-west-1', 'US West (N. California)'), ('us-west-2', 'US West (Oregon)'), ('ca-central-1', 'Canada (Central)'), ('sa-east-1', 'South America (São Paulo)'), ('eu-north-1 ', 'Europe (Stockholm)'), ('eu-west-1', 'Europe (Ireland)'), ('eu-west-2', 'Europe (London)'), ('eu-west-3', 'Europe (Paris)'), ('eu-central-1', 'Europe (Frankfurt)'), ('eu-south-1', 'Europe (Milan)'), ('eu-south-2', 'Europe (Spain)')], default='us-east-1', max_length=30),
        ),
    ]
