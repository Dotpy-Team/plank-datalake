from django import forms
from process.models import Tables,Columns,Dependencies,JobRun


class DependenciesForm(forms.ModelForm):
    SATUS_CHOICES = [
        ('Habilitado', 'Habilitado'),
        ('Desabilitado', 'Desabilitado')
    ]

    str_status = forms.ChoiceField(
        choices=SATUS_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    dth_start_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    dth_last_update = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    class Meta:
        model = Dependencies
        fields = [
            'table_node',
            'table_edge',
            'str_status',
            'dth_start_at',
            'dth_last_update',
    ]