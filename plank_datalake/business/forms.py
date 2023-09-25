from django import forms
from .models import Customer
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserForm(forms.ModelForm):
    id_customer = forms.IntegerField(
        widget=forms.HiddenInput,
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

    str_name = forms.CharField(required=False)
    str_cnpj = forms.CharField(required=False)
    str_address = forms.CharField(required=False)
    str_telefone = forms.CharField(required=False)
    str_email = forms.CharField(required=False)
    str_site = forms.CharField(required=False)
    str_linkedin_profile = forms.CharField(required=False)
    str_contact = forms.CharField(required=False)
    dth_create = forms.DateField(required=False)
    str_finance_complement = forms.CharField(required=False)
    str_documents = forms.CharField(required=False)
    str_comments = forms.CharField(required=False)
    
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