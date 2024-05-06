from django import forms
from process.models import System, DataSet
from business.models import Customer, Task

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

    str_type = forms.CharField(
        label= "Type",
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    str_project_id = forms.CharField(
        label='Project Id',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_private_key_id = forms.CharField(
        label='Private Key Id',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_private_key = forms.CharField(
        label='Private Key',
        widget= forms.Textarea(attrs={'class': 'form-control'})
    )

    str_client_email = forms.CharField(
        label= 'Client E-mail',
        widget= forms.TextInput(attrs={'class':'form-control'}),
        required=True
    )

    str_client_id = forms.CharField(
        label='Client id',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_auth_uri = forms.CharField(
        label='Auth Uri',
        widget=forms.TextInput(attrs={'class': 'form-cotrol'}),
        required=True
    )

    str_token_uri = forms.CharField(
        label='Token Uri',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_auth_provider_x509_cert_url = forms.CharField(
        label='Auth Provider',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_client_x509_cert_url = forms.CharField(
        label='Client Cert Url',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_universe_domain = forms.CharField(
        label='Domain',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:

        model=System
        fields = [
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia',
            'str_type', 
            'str_project_id', 
            'str_private_key_id',
            'str_private_key',
            'str_client_email',
            'str_client_id',
            'str_auth_uri',
            'str_token_uri',
            'str_auth_provider_x509_cert_url',
            'str_client_x509_cert_url',
            'str_universe_domain'   
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

    str_engine = forms.CharField(
        label= 'Engine',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_name = forms.CharField(
        label= 'Name',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_user = forms.CharField(
        label= 'User',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_password = forms.CharField(
        label= 'Password',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_host = forms.CharField(       
        label= 'Host',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_port = forms.CharField(
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
            'str_engine',
            'str_name',
            'str_user',
            'str_password',
            'str_host',
            'str_port'
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

    
    str_user = forms.CharField(
        label= 'User',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_passwd = forms.CharField(
        label='Password',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_database = forms.CharField(
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
            'str_host',
            'str_user',
            'str_passwd',
            'str_database'
        ]


class SQLiteSystemForm(forms.ModelForm):

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

    str_engine = forms.CharField(
        label= 'Engine',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_database_name = forms.CharField(
        label= 'Database Name',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )


    class Meta:
        model  = System 
        fields = [
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia',
            'str_engine',
            'str_database_name'
        ]