from django import forms
from business.models import Service

class ServiceForm(forms.ModelForm):
    
    str_title = forms.CharField(
        label='Nome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_descr = forms.CharField(
        label='Descricao *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    int_price = forms.IntegerField(
        label='Preco *',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )
    
    int_qnt = forms.IntegerField(
        label='Quantidade *',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
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

    class Meta:
        model = Service
        fields = [
            'str_title',
            'str_descr',
            'int_price',
            'int_qnt',
            'str_status'
        ]
