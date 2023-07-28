from django import forms
from .models import Tables,Columns,Dependencies,JobRun


class TablesForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = [
            "id_customer",
            "str_system",
            "str_frequency",
            "str_hour_of",
            "str_mode",
            "str_type",
            "str_dataset",
            "str_name",
            "str_desc",
            "str_owner",
            "str_owner_email"
        ]


class ColumnsForm(forms.ModelForm):
    class Meta:
        model = Columns
        fields = [
        'id_table',
        'str_source_name',
        'str_rename',
        'str_datatype',
        'str_pattern_format',
        'str_type'
        ]


class DependenciesForm(forms.ModelForm):
    class Meta:
        model = Dependencies
        fields = [
            'id_table_node',
            'id_table_edge',
            'str_status',
            'dth_start_at',
            'dth_last_update',
    ]


class JobRunForm(forms.ModelForm):
    class Meta:
        model = JobRun
        fields = [
            'id_job',
            'id_table',
            'dth_last_updated',
            'dth_start_at',
            'int_total_size',
            'int_total_rows'
        ]
