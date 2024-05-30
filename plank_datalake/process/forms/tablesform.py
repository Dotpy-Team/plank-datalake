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

    CHOICE_ARCHIVE_TYPE = (
        ('json', 'json'),
        ('txt', 'txt'),
        ('parquet', 'parquet'),
        ('csv', 'csv')
    )

    str_archive_type = forms.ChoiceField(
        label= 'Tipo de arquivo',
        choices= CHOICE_ARCHIVE_TYPE,
        widget= forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    CHOICE_SEPARADOR = (
        (';', ';'),
        (',', ','),
        ('\t', '\t')
    )

    str_separador = forms.ChoiceField(
        label= 'Separador',
        choices= CHOICE_SEPARADOR,
        widget= forms.Select(attrs={'class': 'form-select'}),
        required= True
    )

    CHOICE_DELIMITADOR = (
        ('\n', '\n'),
        ('n', 'n')
    )

    str_delimitador = forms.ChoiceField(
        label= 'Delimitador',
        choices= CHOICE_DELIMITADOR,
        widget= forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    CHOICE_HEADER = (
        ('True', 'True'),
        ('False', 'False')
    )

    str_header = forms.ChoiceField(
        label= 'Header',
        choices= CHOICE_HEADER,
        widget= forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    CHOICE_TRAILER = (
        ('True', 'True'),
        ('False', 'False')
    )

    str_trailer = forms.ChoiceField(
        label='Trailer',
        choices= CHOICE_TRAILER,
        widget= forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    str_key_word = forms.CharField(
        label= 'Key Word',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
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
            "str_archive_type",
            "str_separador",
            "str_delimitador",
            "str_header",
            "str_trailer",
            "str_key_word",
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

    CHOICE_ARCHIVE_TYPE = (
        ('json', 'json'),
        ('txt', 'txt'),
        ('parquet', 'parquet'),
        ('csv', 'csv')
    )

    str_archive_type = forms.ChoiceField(
        label= 'Tipo de arquivo',
        choices= CHOICE_ARCHIVE_TYPE,
        widget= forms.Select(attrs={'form': 'form-select'}),
        required=True
    )

    CHOICE_SEPARADOR = (
        (';', ';'),
        (',', ','),
        ('\t', '\t')
    )

    str_separador = forms.ChoiceField(
        label= 'Separador',
        choices= CHOICE_SEPARADOR,
        widget= forms.Select(attrs={'form': 'form-select'}),
        required= True
    )

    CHOICE_DELIMITADOR = (
        ('\n', '\n')
    )

    str_delimitador = forms.ChoiceField(
        label= 'Delimitador',
        choices= CHOICE_DELIMITADOR,
        widget= forms.Select(attrs={'form': 'form-select'}),
        required=True
    )

    CHOICE_HEADER = (
        ('True', 'True'),
        ('False', 'False')
    )

    str_header = forms.ChoiceField(
        label= 'Header',
        choices= CHOICE_HEADER,
        widget= forms.Select(attrs={'form': 'form-select'}),
        required=True
    )

    CHOICE_TRAILER = (
        ('True', 'True'),
        ('False', 'False')
    )

    str_trailer = forms.ChoiceField(
        label='Trailer',
        choices= CHOICE_TRAILER,
        widget= forms.Select(attrs={'form': 'form-select'}),
        required=True
    )

    str_key_word = forms.CharField(
        label='Key Word',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
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
            "str_archive_type",
            "str_separador",
            "str_delimitador",
            "str_header",
            "str_trailer",
            "str_key_word",
            "trigger"
        ]


