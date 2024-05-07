from django import forms 
from process.models import Pipeline 


class PipelineForm(forms.ModelForm):
    str_title = forms.CharField(
        label = 'Titulo',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True 
    )

    dth_start_at = forms.DateTimeField(
        label= 'Data de Inicio', 
        widget= forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    dth_end_at = forms.DateTimeField(
        label= 'Data do Fim',
        widget= forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
    )

    str_desc = forms.CharField(
        label= 'Descrição',
        widget= forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta: 
        model = Pipeline
        fields = [
            'str_title',
            'dth_start_at',
            'dth_end_at',
            'str_desc',
            'raci_activity'
        ]