from django import forms
from .models import Tables,Columns,WorkLoads,Dependencies,JobRun


class TablesForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = [
            "id_customer",
            "id_workload",
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
        'str_from_datatype',
        'str_datatype_to_apply',
        'str_pattern_format',
        'str_primary_key',
        'str_change_data_capture',
        'str_desc'
        ]

class WorkLoadsForm(forms.ModelForm):
    class Meta:
        model = WorkLoads
        fields = [
            'id_workload', 
            'id_customer',
            'id_table',
            'str_project',
            'str_relative_import',
            'dth_last_updated',
            'dth_start_at'
        ]


class DependenciesForm(forms.ModelForm):
    class Meta:
        model = Dependencies
        fields = [
            'id_workload_node',
            'id_workload_edge',
            'str_status',
            'dth_start_at'
    ]


class JobRunForm(forms.ModelForm):
    class Meta:
        model = JobRun
        fields = [
            'id_job',
            'id_workload',
            'dth_last_updated',
            'dth_start_at',
            'int_total_size',
            'int_total_rows'
        ]
