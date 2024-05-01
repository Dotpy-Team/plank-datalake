from django import forms
from process.models import Tables

class TablesForm(forms.ModelForm):
    CHOICES_FREQUENCY = (
        ('Daily', 'Diario'), 
        ('Montly', 'Mensal'), 
        ('Hour', 'A cada 1 hora'), 
        ('Weekly', 'Semanal')
    )

    str_frequency = forms.ChoiceField(
        label='Frequencia:',
        choices=CHOICES_FREQUENCY,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    CHOICES_TYPE_OF = (
        ('Procedure', 'Procedure'), 
        ('Ingestion', 'Ingestion'), 
        ('Copy', 'Copy')
    )

    str_type_of = forms.ChoiceField(
        label='Modo:',
        choices=CHOICES_TYPE_OF,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )


    CHOICES_MODE = (
        ('Batch', 'Batch'), 
        ('Incremental', 'Incremental')
    )

    str_mode = forms.ChoiceField(
        label='Modo:',
        choices=CHOICES_MODE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    CHOICES_TYPE = (
        ('CDC', 'Detecte as Mudanças'),
        ('ULP', 'Considere a Ultima Particao')
    )

    str_type = forms.ChoiceField(
        label='Modo:',
        choices=CHOICES_TYPE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    str_name = forms.CharField(
        label='Nome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_desc = forms.CharField(
        label='Descricao *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_desc_ia = forms.CharField(
        label='Descricao *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
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
        model = Tables
        fields = [
            "str_frequency",
            "str_type_of",
            "str_mode",
            "str_type",
            "str_name",
            "str_desc",
            "str_desc_ia",
            "str_color",
            "trigger"
        ]

class TablesStepForm(forms.ModelForm):

    CHOICES_FREQUENCY = (
        ('Daily', 'Diario'), 
        ('Montly', 'Mensal'), 
        ('Hour', 'A cada 1 hora'), 
        ('Weekly', 'Semanal')
    )

    str_frequency = forms.ChoiceField(
        label='Frequencia:',
        choices=CHOICES_FREQUENCY,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    CHOICES_TYPE_OF = (
        ('Procedure', 'Procedure'), 
        ('Ingestion', 'Ingestion'), 
        ('Copy', 'Copy')
    )

    str_type_of = forms.ChoiceField(
        label='Modo:',
        choices=CHOICES_TYPE_OF,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )


    CHOICES_MODE = (
        ('Batch', 'Batch'), 
        ('Incremental', 'Incremental')
    )

    str_mode = forms.ChoiceField(
        label='Modo:',
        choices=CHOICES_MODE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    CHOICES_TYPE = (
        ('CDC', 'Detecte as Mudanças'),
        ('ULP', 'Considere a Ultima Particao')
    )

    str_type = forms.ChoiceField(
        label='Modo:',
        choices=CHOICES_TYPE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    str_name = forms.CharField(
        label='Nome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_desc = forms.CharField(
        label='Descricao *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_desc_ia = forms.CharField(
        label='Descricao *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )


    class Meta:
        model = Tables
        fields = [
            "str_frequency",
            "str_type_of",
            "str_mode",
            "str_type",
            "str_name",
            "str_desc",
            "str_desc_ia",
            "str_color",
            "trigger"
        ]


