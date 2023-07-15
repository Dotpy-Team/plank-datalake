from django import forms
from .models import Tables


class TablesForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = [
            "id_customer",
            "id_workload",
            "str_system",
            "str_frequency",
            "int_hour_of",
            "str_mode",
            "str_type",
            "str_dataset",
            "str_name",
            "str_desc",
            "str_owner",
            "str_owner_email",
            "dth_last_updated",
            "int_size",
            "int_number_of_rows",
            "float_perc_growth",
            "str_id_version"
        ]