from django import forms
from business.models import Task

class TaskForm(forms.ModelForm):
    id_customer = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False
    )
    id_table = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=False
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
    str_documents = forms.FileField(
        label='Anexos:',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False  # Se necessário, dependendo da sua lógica
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

    dth_start_at = forms.DateField(
        label='Data de Inicio *',  # Rótulo personalizado
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    dth_end_at = forms.DateField(
        label='Prazo Final *',  # Rótulo personalizado
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    class Meta:
        model = Task
        fields = [
            'id_customer',
            'id_table',
            'str_title',
            'str_desc',
            'str_documents',
            'str_status',
            'dth_start_at',
            'dth_end_at'
        ]
