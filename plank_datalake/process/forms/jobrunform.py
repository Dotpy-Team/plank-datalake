from django import forms
from process.models import JobRun

class JobRunForm(forms.ModelForm):
    # dth_last_updated = models.DateTimeField()
    # dth_start_at = models.DateTimeField()
    # str_status = models.CharField(max_length=200)
    # int_total_size = models.IntegerField()
    # int_total_rows = models.IntegerField()

    dth_last_updated = forms.DateField(
        label='Data de criação *',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    dth_start_at = forms.DateField(
        label='Data de Inicio *',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    CHOICES_STATUS = (
        ('F', 'Finished'),
        ('S', 'Started'),
        ('A', 'Aborted'),
        ('E', 'Error')
    )

    str_status = forms.ChoiceField(
        label='Status:',
        choices=CHOICES_STATUS,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    int_total_size = forms.IntegerField(
        label='Tamanho total:',
        widget=forms.NumberInput(attrs={'class': 'form-control mt-1'}),
        required=True
    )

    int_total_rows = forms.IntegerField(
        label='quantidade de linhas processadas:',
        widget=forms.NumberInput(attrs={'class': 'form-control mt-1'}),
        required=True
    )

    class Meta:
        model = JobRun
        fields = [
            'dth_last_updated',
            'dth_start_at',
            'str_status',
            'int_total_size',
            'int_total_rows'
        ]