from django import forms 
from process.models import Conector


class SheetConfigForm(forms.ModelForm):
    conector_name = forms.CharField(
        label='Nome do conector',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

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
            'conector_name',
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
        

class PostConfigForm(forms.ModelForm):
    conector_name = forms.CharField(
        label='Nome do conector',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    engine = forms.CharField(
        label= 'Engine',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    name = forms.CharField(
        label= 'Name',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    user = forms.CharField(
        label= 'User',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    password = forms.CharField(
        label= 'Password',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    host = forms.CharField(       
        label= 'Host',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    port = forms.CharField(
        label= 'Port',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Conector
        fields = [
            'conector_name', 
            'engine',
            'name',
            'user',
            'password',
            'host',
            'port'
        ]


class MySqlConfigForm(forms.ModelForm):
    conector_name = forms.CharField(
        label='Nome do conector',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    host = forms.CharField(       
        label= 'Host',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    user = forms.CharField(
        label= 'User',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    passwd = forms.CharField(
        label='Password',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    database = forms.CharField(
        label='Database',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Conector
        fields = [
            'conector_name',
            'host',
            'user',
            'passwd',
            'database'
        ]
