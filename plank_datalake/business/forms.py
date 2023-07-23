from django import forms
from .models import CustomUser, Customer

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    str_cpf = forms.CharField(required=False)
    str_telefone = forms.CharField(required=False)
    str_cargo = forms.CharField(required=False)
    id_company = forms.IntegerField(required=False)

    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'password', 
            'first_name', 
            'last_name', 
            'str_cpf', 
            'str_telefone',
            'id_company',
            'str_cargo'
        ]

class CustomerForm(forms.ModelForm):
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