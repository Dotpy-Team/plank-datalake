from django import forms
from process.models import Tables,Columns,Dependencies,JobRun


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