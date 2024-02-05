from django import forms 
from process.models import Conector


class SheetConfigForm(forms.ModelForm):
    type = forms.CharField(
        label= "Type",
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    project_id = forms.CharField(
        label='Project Id',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    private_key_id = forms.CharField(
        label='Private Key Id',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    private_key = forms.CharField(
        label='Private Key',
        widget= forms.Textarea(attrs={'class': 'form-control'})
    )

    client_email = forms.CharField(
        label= 'Client E-mail',
        widget= forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )

    client_id = forms.CharField(
        label='Client id',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    auth_uri = forms.CharField(
        label= 'Auth Uri',
        widget= forms.TextInput(attrs={'class': 'form-cotrol'}),
        required= True
    )

    token_uri = forms.CharField(
        label= 'Token Uri',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    auth_provider_x509_cert_url = forms.CharField(
        label= 'Auth Provider',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    client_x509_cert_url = forms.CharField(
        label= 'Client Cert Url',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    universe_domain = forms.CharField(
        label= 'Domain',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )


    class Meta:
        model = Conector
        fields= [
            'type', 
            'project_id', 
            'private_key_id',
            'private_key',
            'client_email',
            'client_id',
            'auth_uri',
            'token_uri',
            'auth_provider_x509_cert_url',
            'client_x509_cert_url',
            'universe_domain'
        ]