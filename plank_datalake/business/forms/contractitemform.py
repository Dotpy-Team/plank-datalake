from business.models.contractitem import ContractItem
from business.models.service import Service
from business.models.contract import Contract
from django import forms

class ContractItemForm(forms.ModelForm):

    id_service = forms.ModelChoiceField(
        queryset=Service.objects.all()
    )

    class Meta:
        model = ContractItem
        fields = ['id_service']
