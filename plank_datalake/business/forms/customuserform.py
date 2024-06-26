from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserForm(forms.ModelForm):
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

    str_address_number = forms.CharField(
        label='Número',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_postal_cod = forms.CharField(
        label="CEP",
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
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
            'first_name', 
            'last_name',
            'str_cpf', 
            'str_telefone',
            'str_cargo',
            'str_address',
            'str_address_number',
            'str_postal_cod',
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