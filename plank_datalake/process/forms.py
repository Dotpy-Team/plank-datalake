from django import forms
from .models import Tables,Columns,Dependencies,JobRun


class TablesForm(forms.ModelForm):

    id_customer = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=True
    )

    str_system = forms.CharField(
        label='Systema *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

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

    str_hour_of = forms.CharField(
        label='Horário *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
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

    CHOICES_DATASET = (
        ('CAD', 'Cadastro'),
        ('TRAN', 'Transacional'),
        ('LOG', 'Traking'),
        ('JUD', 'Juridico'),
        ('TECH', 'Tecnologia'),
        ('ADM', 'Administrativo'),
        ('FUP', 'Follow Up'),
        ('IOT', 'Sensores'),
        ('MED', 'Registros Medicos'),
        ('FAT', 'Faturamento')
    )

    str_dataset = forms.ChoiceField(
        label='Dataset:',
        choices=CHOICES_DATASET,
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

    str_owner = forms.CharField(
        label='owner *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_owner_email = forms.EmailField(
        label='Email *',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Tables
        fields = [
            "id_customer",
            "str_system",
            "str_frequency",
            "str_hour_of",
            "str_mode",
            "str_type",
            "str_dataset",
            "str_name",
            "str_desc",
            "str_owner",
            "str_owner_email"
        ]


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


class DependenciesForm(forms.ModelForm):
    class Meta:
        model = Dependencies
        fields = [
            'id_table_node',
            'id_table_edge',
            'str_status',
            'dth_start_at',
            'dth_last_update',
    ]


class JobRunForm(forms.ModelForm):
    class Meta:
        model = JobRun
        fields = [
            'id_job',
            'id_table',
            'dth_last_updated',
            'dth_start_at',
            'int_total_size',
            'int_total_rows'
        ]
