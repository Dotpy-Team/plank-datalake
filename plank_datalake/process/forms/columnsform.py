from django import forms
from process.models import Columns

class ColumnsForm(forms.ModelForm):

    str_source_name = forms.CharField(
        label='Nome na Origem:*',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_rename = forms.CharField(
        label='Nome no Destino:*',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    CHOICES_DATATYPE = (
        ('string', 'String'),
        ('int', 'Integer'),
        ('bigint', 'BigInt'),
        ('double', 'Float'),
        ('timestamp', 'Date'),
        ('timestamp', 'Datetime')
    )

    str_datatype = forms.ChoiceField(
        label='Datatype:',
        choices=CHOICES_DATATYPE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    str_pattern_format = forms.CharField(
        label='Padrão:',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    CHOICES_TYPE = (
        ('CPK', 'Chave Primaria.'),
        ('CFK', 'Chave Extrangeira.'),
        ('KDS', 'Campo Descritivo.'),
        ('SEN','Dados Sensiveis')
    )

    str_type = forms.ChoiceField(
        label='Datatype:',
        choices=CHOICES_TYPE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    class Meta:
        model = Columns
        fields = [
            'str_source_name',
            'str_rename',
            'str_datatype',
            'str_pattern_format',
            'str_type'
        ]
