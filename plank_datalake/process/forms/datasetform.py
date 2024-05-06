from django import forms
from process.models import  DataSet

class DataSetForm(forms.ModelForm):
    
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

    CHOICE_COLOR = (
        ('R', 'red'),
        ('g', 'green'),
        ('b', 'blue')
    )

    str_color = forms.ChoiceField(
        label='cor',
        choices=CHOICE_COLOR,
        widget= forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    class Meta:
        model = DataSet
        fields = [
            'str_status',
            'str_title',
            'str_desc',
            'raci_activity',
            'str_color',
            'str_desc_ia'
        ]
