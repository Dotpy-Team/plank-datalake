from django import forms
from process.models import Columns

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
