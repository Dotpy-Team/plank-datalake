from django import forms
from process.models import Tables,Columns,Dependencies,JobRun

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