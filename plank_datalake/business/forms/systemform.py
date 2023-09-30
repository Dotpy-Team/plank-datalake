from django import forms
from business.models import Customer, System , DataSet , Task

class SystemForm(forms.ModelForm):
    id_customer = forms.IntegerField(
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
        model = System
        fields = [
            'id_customer',
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia'

        ]
