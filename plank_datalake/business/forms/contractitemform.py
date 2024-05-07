from business.models.contractitem import ContractItem
from business.models.service import Service
from business.models.contract import Contract
from django import forms


class ContractItemForm(forms.ModelForm):

    class Meta:
        model = ContractItem
        fields = ['service']
