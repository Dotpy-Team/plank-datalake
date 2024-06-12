# Generated by Django 4.2.6 on 2024-06-12 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfCluster',
            fields=[
                ('id_cluster', models.AutoField(primary_key=True, serialize=False)),
                ('str_worker_type', models.CharField(blank=True, max_length=200, null=True)),
                ('str_numer_of_workers', models.CharField(blank=True, max_length=200, null=True)),
                ('int_time_out', models.IntegerField()),
                ('int_max_capacity', models.IntegerField()),
                ('str_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_title', models.CharField(blank=True, max_length=200, null=True)),
                ('str_object', models.CharField(blank=True, max_length=200, null=True)),
                ('str_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=20)),
                ('dth_created_at', models.DateField(auto_now=True)),
                ('dth_start_at', models.DateField()),
                ('dth_end_at', models.DateField()),
                ('dth_updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_customer_type', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Prospec', 'Prospec'), ('Teste', 'Teste'), ('Admin', 'Admin')], max_length=20)),
                ('str_name', models.CharField(blank=True, max_length=200, null=True)),
                ('str_cnpj', models.CharField(blank=True, max_length=200, null=True)),
                ('str_address', models.CharField(blank=True, max_length=200, null=True)),
                ('str_telefone', models.CharField(blank=True, max_length=200, null=True)),
                ('str_email', models.CharField(max_length=200)),
                ('str_site', models.CharField(max_length=200)),
                ('str_linkedin_profile', models.CharField(blank=True, max_length=200, null=True)),
                ('str_contact', models.CharField(blank=True, max_length=200, null=True)),
                ('str_setor', models.CharField(choices=[('TECH', 'Tecnologia'), ('ADM', 'Administrativo'), ('JUR', 'Jurídico'), ('FIN', 'Financeiro'), ('SAU', 'Saúde'), ('EDU', 'Educação'), ('COM', 'Comunicação'), ('ART', 'Arte e Cultura'), ('AGR', 'Agrícola'), ('IND', 'Industrial'), ('ALI', 'Alimentício'), ('AUT', 'Automotivo'), ('CON', 'Construção'), ('SER', 'Serviços'), ('PET', 'Petróleo e Gás'), ('MEI', 'Microempreendedor Individual'), ('OUT', 'Outros')], max_length=20)),
                ('str_size', models.CharField(choices=[('PEQ', 'Pequena'), ('PEQ_MEDIA', 'Pequena/Média'), ('MEDIA', 'Média'), ('MEDIA_GRANDE', 'Média/Grande'), ('GRANDE', 'Grande')], max_length=20)),
                ('dth_create', models.DateField()),
                ('dth_start_at', models.DateField(auto_now=True)),
                ('str_finance_complement', models.CharField(max_length=500)),
                ('str_documents', models.CharField(blank=True, max_length=200, null=True)),
                ('str_comments', models.CharField(blank=True, max_length=200, null=True)),
                ('str_cod_aws_account', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('layer_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_title', models.CharField(blank=True, max_length=200, null=True)),
                ('str_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('str_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_title', models.CharField(blank=True, max_length=200, null=True)),
                ('str_descr', models.CharField(blank=True, max_length=200, null=True)),
                ('int_price', models.IntegerField(blank=True, null=True)),
                ('int_qnt', models.IntegerField(blank=True, null=True)),
                ('str_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=20)),
                ('dth_created_at', models.DateField(auto_now=True)),
                ('dth_updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('table', models.IntegerField(blank=True, null=True)),
                ('str_title', models.CharField(blank=True, max_length=200, null=True)),
                ('str_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('str_documents', models.CharField(blank=True, max_length=200, null=True)),
                ('str_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], max_length=20)),
                ('dth_create', models.DateField(auto_now=True)),
                ('dth_start_at', models.DateField()),
                ('dth_end_at', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ContractItem',
            fields=[
                ('contractitem_id', models.AutoField(primary_key=True, serialize=False)),
                ('dth_created_at', models.DateField(auto_now=True)),
                ('dth_updated_at', models.DateField(auto_now=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.contract')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.service')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer'),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_first_name', models.CharField(max_length=80)),
                ('str_last_name', models.CharField(max_length=80)),
                ('str_email', models.CharField(max_length=80)),
                ('str_comercial_email', models.CharField(max_length=80)),
                ('str_phone_number', models.CharField(max_length=20)),
                ('str_comercial_phone_number', models.CharField(max_length=20)),
                ('str_whatsapp_number', models.CharField(max_length=20)),
                ('str_type_contact', models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee')], max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('str_cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('str_telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('str_cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('str_address', models.CharField(max_length=100)),
                ('str_address_number', models.CharField(max_length=20)),
                ('str_postal_cod', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.customer')),
                ('groups', models.ManyToManyField(related_name='custom_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_users', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
