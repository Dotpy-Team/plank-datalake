# Generated by Django 4.2.6 on 2024-08-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0003_alter_columns_str_datatype'),
    ]

    operations = [
        migrations.AddField(
            model_name='raciactivity',
            name='str_status',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
