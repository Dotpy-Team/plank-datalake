from django import forms 
from process.models import Step


class StepForm(forms.ModelForm):
    str_query = forms.CharField(
        label='Query',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Step
        fields = [
            'str_query'
        ]

