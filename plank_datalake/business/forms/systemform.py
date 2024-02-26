from django import forms
from business.models import Customer, System , DataSet , Task

class SystemForm(forms.ModelForm):

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

    class Meta:
        model = System
        fields = [
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia'
        ]

class GoogleSheetSystemForm(forms.ModelForm):

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
        model= System
        fields = [
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia',
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

class PostGreSytemForm(forms.ModelForm):
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
        model = System
        fields = [
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia',
            'engine',
            'name',
            'user',
            'password',
            'host',
            'port'
        ]

class MySqlSystemForm(forms.ModelForm):

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
        model  = System 
        fields = [
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia',
            'host',
            'user',
            'passwd',
            'database'
        ]