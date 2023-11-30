from django import forms
from business.models.contract import Contract

class ContractForm(forms.ModelForm):
    str_title = forms.CharField(
        label='Titulo *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_object = forms.CharField(
        label='Descrição *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    CHOICES_STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )

    str_status = forms.ChoiceField(
        label='Status do Contrato:',
        choices=CHOICES_STATUS,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    dth_start_at = forms.DateField(
        label='Data de Início *',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    dth_end_at = forms.DateField(
        label='Data de Término *',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    class Meta:
        model = Contract
        fields = [
            'str_title',
            'str_object',
            'str_status',
            'dth_start_at',
            'dth_end_at'
        ]
