# Generated by Django 4.2.6 on 2024-06-12 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('dataset_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=20)),
                ('str_title', models.CharField(blank=True, max_length=200, null=True)),
                ('str_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('str_desc_ia', models.CharField(blank=True, max_length=200, null=True)),
                ('dth_start_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('pipeline_id', models.AutoField(primary_key=True, serialize=False)),
                ('dth_start_at', models.DateTimeField()),
                ('dth_end_at', models.DateTimeField()),
                ('str_title', models.CharField(max_length=80)),
                ('str_desc', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
            ],
        ),
        migrations.CreateModel(
            name='RaciActivity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_title', models.CharField(max_length=200)),
                ('str_desc', models.CharField(max_length=200)),
                ('dth_created_at', models.DateTimeField(auto_now_add=True)),
                ('str_shareable', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=30)),
                ('str_color', models.CharField(choices=[('red', 'red'), ('green', 'green'), ('blue', 'blue')], max_length=30)),
                ('accountable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountable', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsible', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('step_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_query', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('pipeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.pipeline')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('trigger_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_cron', models.TextField()),
                ('str_title', models.CharField(max_length=80)),
                ('str_status', models.CharField(max_length=21)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_name', models.CharField(max_length=80)),
                ('str_desc', models.TextField()),
                ('str_desc_ia', models.TextField()),
                ('dth_start_at', models.DateTimeField(auto_now=True)),
                ('dth_last_updated', models.DateTimeField(blank=True, null=True)),
                ('int_size', models.IntegerField(blank=True, null=True)),
                ('int_number_of_rows', models.IntegerField(blank=True, null=True)),
                ('float_perc_growth', models.FloatField(blank=True, null=True)),
                ('str_key_words', models.CharField(max_length=100)),
                ('layer', models.CharField(max_length=20)),
                ('str_frequency', models.CharField(blank=True, choices=[('Daily', 'Diario'), ('Montly', 'Mensal'), ('Hour', 'A cada 1 hora'), ('Weekly', 'Semanal')], max_length=20, null=True)),
                ('str_type_of', models.CharField(blank=True, choices=[('Procedure', 'Procedure'), ('Ingestion', 'Ingestion'), ('Copy', 'Copy')], max_length=20, null=True)),
                ('str_mode', models.CharField(blank=True, choices=[('Batch', 'Batch'), ('Incremental', 'Incremental')], max_length=20, null=True)),
                ('str_type', models.CharField(blank=True, choices=[('CDC', 'Detecte as Mudanças'), ('FULL', 'Considere a Ultima Particao')], max_length=20, null=True)),
                ('str_archive_type', models.CharField(choices=[('json', 'json'), ('txt', 'txt'), ('parquet', 'parquet'), ('csv', 'csv')], max_length=20)),
                ('str_separador', models.CharField(choices=[(';', ';'), (',', ','), ('\t', '\t')], max_length=10)),
                ('str_delimitador', models.CharField(choices=[('\n', '\n'), ('n', 'n')], max_length=10)),
                ('str_header', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('str_trailer', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('dataset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='process.dataset')),
                ('step', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='process.step')),
                ('trigger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='process.trigger')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('system_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=20)),
                ('str_title', models.CharField(blank=True, max_length=200, null=True)),
                ('str_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('str_desc_ia', models.CharField(blank=True, max_length=200, null=True)),
                ('dth_start_at', models.DateField(auto_now=True)),
                ('str_system_type', models.CharField(max_length=50)),
                ('str_type', models.CharField(blank=True, max_length=80, null=True)),
                ('str_project_id', models.CharField(blank=True, max_length=80, null=True)),
                ('str_private_key_id', models.CharField(blank=True, max_length=100, null=True)),
                ('str_private_key', models.TextField(blank=True, null=True)),
                ('str_client_email', models.CharField(blank=True, max_length=100, null=True)),
                ('str_client_id', models.CharField(blank=True, max_length=80, null=True)),
                ('str_auth_uri', models.CharField(blank=True, max_length=80, null=True)),
                ('str_token_uri', models.CharField(blank=True, max_length=80, null=True)),
                ('str_auth_provider_x509_cert_url', models.CharField(blank=True, max_length=80, null=True)),
                ('str_client_x509_cert_url', models.CharField(blank=True, max_length=200, null=True)),
                ('str_universe_domain', models.CharField(blank=True, max_length=50, null=True)),
                ('str_engine', models.CharField(blank=True, max_length=100, null=True)),
                ('str_name', models.CharField(blank=True, max_length=80, null=True)),
                ('str_user', models.CharField(blank=True, max_length=80, null=True)),
                ('str_password', models.CharField(blank=True, max_length=50, null=True)),
                ('str_host', models.CharField(blank=True, max_length=80, null=True)),
                ('str_port', models.CharField(blank=True, max_length=80, null=True)),
                ('str_passwd', models.CharField(blank=True, max_length=50, null=True)),
                ('str_database', models.CharField(blank=True, max_length=80, null=True)),
                ('str_database_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
            ],
        ),
        migrations.CreateModel(
            name='RaciRelated',
            fields=[
                ('related_id', models.AutoField(primary_key=True, serialize=False)),
                ('dth_add', models.DateTimeField(auto_now_add=True)),
                ('str_type', models.CharField(choices=[('CON', 'Consultado'), ('INF', 'Informado')], max_length=20)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.raciactivity')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pipeline',
            name='raci_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.raciactivity'),
        ),
        migrations.CreateModel(
            name='LogRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_url', models.CharField(max_length=200)),
                ('str_method', models.CharField(max_length=80)),
                ('str_request_body', models.TextField()),
                ('str_response_status', models.IntegerField()),
                ('str_response_body', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
            ],
        ),
        migrations.CreateModel(
            name='JobRun',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('dth_last_updated', models.DateTimeField()),
                ('dth_start_at', models.DateTimeField()),
                ('str_status', models.CharField(max_length=200)),
                ('int_total_size', models.IntegerField()),
                ('int_total_rows', models.IntegerField()),
                ('str_event_bucket_trigger', models.CharField(max_length=100)),
                ('str_event_key_trigger', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.tables')),
            ],
        ),
        migrations.CreateModel(
            name='Dependencies',
            fields=[
                ('dependency_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('table_edge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_edge', to='process.tables')),
                ('table_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_node', to='process.tables')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='raci_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='process.raciactivity'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.system'),
        ),
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id_column', models.AutoField(primary_key=True, serialize=False)),
                ('str_source_name', models.CharField(max_length=60)),
                ('str_rename', models.CharField(max_length=60)),
                ('str_datatype', models.CharField(choices=[('STR', 'String'), ('INT', 'Integer'), ('FLO', 'Float'), ('DAT', 'Date'), ('DTH', 'Datetime')], max_length=60)),
                ('str_pattern_format', models.CharField(max_length=60)),
                ('str_type', models.CharField(choices=[('CPK', 'Chave Primaria.'), ('CFK', 'Chave Extrangeira.'), ('KDS', 'Campo Descritivo.'), ('SEN', 'Dados Sensiveis')], max_length=20)),
                ('str_desc', models.CharField(max_length=60)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.tables')),
            ],
        ),
    ]