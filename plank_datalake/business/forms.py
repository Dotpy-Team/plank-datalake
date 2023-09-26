from django import forms
from .models import Customer, System , DataSet
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserForm(forms.ModelForm):
    id_customer = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=True
    )
    first_name = forms.CharField(
        label='Nome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    last_name = forms.CharField(
        label='Sobrenome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_cpf = forms.CharField(
        label='CPF *',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '000.000.000-00'}),
        required=True
    )
    str_telefone = forms.CharField(
        label='Telefone *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_cargo = forms.CharField(
        label='Cargo',
        widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False
    )

    str_address = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False
    )

    email = forms.EmailField(
        label='Email *',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False
    )

    password = forms.CharField(
        label='Senha *',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'id_customer',
            'first_name', 
            'last_name',
            'str_cpf', 
            'str_telefone',
            'str_cargo',
            'str_address',
            'email', 
            'password'
        ]

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user

class CustomerForm(forms.ModelForm):

    str_name = forms.CharField(
        label='Nome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_cnpj = forms.CharField(
        label='CNPJ *',
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': '00.000.000/0001-00'}),
        required=True
    )
    str_address = forms.CharField(
        label='Endereço *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_telefone = forms.CharField(
        label='Telefone de contato *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_email = forms.EmailField(
        label='Email *',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=False
    )
    str_site = forms.CharField(
        label='Site *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    str_linkedin_profile = forms.CharField(
        label='Perfil no Linkedin *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_contact = forms.CharField(
        label='Outros Contatos *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    dth_create = forms.DateField(
        label='Data de Criação *',  # Rótulo personalizado
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    str_finance_complement = forms.CharField(
        label='Complementos Financeiros *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    str_documents = forms.FileField(
        label='Outros complementos:',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False  # Se necessário, dependendo da sua lógica
    )
    str_comments = forms.CharField(
        label='Outros Comentários *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
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
            'str_comments'
        ]


class SystemForm(forms.ModelForm):
    id_customer = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=True
    )

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
            'id_customer',
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia'

        ]

class DataSetForm(forms.ModelForm):
    id_system = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=True
    )

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
        model = DataSet
        fields = [
            'id_system',
            'str_status',
            'str_title',
            'str_desc',
            'str_desc_ia'
        ]
