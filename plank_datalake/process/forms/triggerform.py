from django import forms
from process.models import Trigger


class TriggerForm(forms.ModelForm):

    str_cron = forms.CharField(
        label="Cron",
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    str_title = forms.CharField(
        label= 'Titulo',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    str_status = forms.CharField(
        label= 'Status',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    class Meta:
        model = Trigger
        fields = [
            'str_cron',
            'str_title',
            'str_status'
        ]