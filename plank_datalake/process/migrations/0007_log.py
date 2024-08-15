# Generated by Django 4.2.6 on 2024-08-15 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0006_rename_str_context_id_jobrun_str_jr_context_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('dth_event_at', models.DateTimeField()),
                ('str_type', models.CharField(choices=[('INFO', 'INFO'), ('WARNING', 'WARNING'), ('ERROR', 'ERROR')], max_length=20)),
                ('str_desc', models.CharField(blank=True, max_length=100, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.jobrun')),
            ],
        ),
    ]
