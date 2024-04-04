from django import forms
from business.models import Customer


class CustomerForm(forms.ModelForm):

    str_name = forms.CharField(
        label='Nome completo *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_cnpj = forms.CharField(
        label='CNPJ *',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '00.000.000/0001-00'}),
        required=True
    )
    str_address = forms.CharField(
        label='Endereço completo *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_telefone = forms.CharField(
        label='Telefone de contato *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False
    )
    str_site = forms.CharField(
        label='Site',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    str_linkedin_profile = forms.CharField(
        label='Perfil no Linkedin *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_contact = forms.CharField(
        label='Outros contatos *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    dth_create = forms.DateField(
        label='Data de criação *',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    str_finance_complement = forms.CharField(
        label='Complementos financeiros *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_comments = forms.CharField(
        label='Outros comentários *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_documents = forms.FileField(
        label='Outros complementos',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )


    CHOICES_TYPE = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'), 
        ('Prospec', 'Prospec'),
        ('Teste', 'Teste'),
        ('Admin', 'Admin')
    )
    str_customer_type = forms.ChoiceField(
        label='Status:',
        choices=CHOICES_TYPE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    CHOICES_SIZE = (
        ('PEQ', 'PEQ'),
        ('PEQ MEDIA', 'PEQ MEDIA'), 
        ('MEDIA', 'MEDIA'),
        ('MEDIA GRANDE', 'MEDIA GRANDE'),
        ('GRANDE', 'GRANDE')
    )
    str_size = forms.ChoiceField(
        label='Status:',
        choices=CHOICES_SIZE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    CHOICES_SETOR = (
        ('TECH', 'TECH'),
        ('ADM', 'ADM'), 
        ('JUR', 'JUR'),
        ('FIN', 'FIN'),
        ('LOG', 'LOG')
    )
    str_setor = forms.ChoiceField(
        label='SETOR:',
        choices=CHOICES_SETOR,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )

    cod_aws_account = forms.CharField(
        label= "Código da conta AWS:",
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )
    
    class Meta:
        model = Customer
        fields = [
            'str_customer_type',
            'str_name',
            'str_cnpj',
            'str_address',
            'str_telefone',
            'str_email',
            'str_site',
            'str_linkedin_profile',
            'str_contact',
            'str_setor',
            'str_size',
            'dth_create',
            'str_finance_complement',
            'str_documents',
            'str_comments', 
            'cod_aws_account'
        ]
