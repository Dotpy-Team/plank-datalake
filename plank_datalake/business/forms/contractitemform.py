from business.models.contractitem import ContractItem
from business.models.service import Service
from business.models.contract import Contract
from django import forms

class ContractItemForm(forms.ModelForm):

    service_id = forms.ModelChoiceField(
        queryset=Service.objects.all()
    )

    class Meta:
        model = ContractItem
        fields = ['service_id']
