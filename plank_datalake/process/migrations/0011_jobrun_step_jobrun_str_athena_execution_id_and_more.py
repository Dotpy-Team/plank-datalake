# Generated by Django 4.2.6 on 2024-09-24 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0010_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrun',
            name='step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='process.step'),
        ),
        migrations.AddField(
            model_name='jobrun',
            name='str_athena_execution_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobrun',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='process.tables'),
        ),
    ]
