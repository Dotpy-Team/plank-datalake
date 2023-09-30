from django import forms
from business.models import  DataSet

class DataSetForm(forms.ModelForm):
    id_system = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=True
    )
    CHOICES_STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )

    str_status = forms.ChoiceField(
        label='Status do Sistema:',
        choices=CHOICES_STATUS,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )
    str_title = forms.CharField(
        label='Nome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_desc = forms.CharField(
        label='Descricao *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = DataSet
        fields = [
            'id_system',
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia'
        ]
