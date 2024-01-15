from django import forms 
from business.models import Contacts


class ContactsForm(forms.ModelForm):
    str_name = forms.CharField(
        label='Nome', 
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.CharField(
        label='Email',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_phone_number = forms.CharField(
        label = 'Telefone',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    CONTACT_CHOICES = (
        ('Admin', 'Admin'),
        ('Employee', 'Employee')
    )

    str_type_contact = forms.ChoiceField(
        label='Cargo',
        choices = CONTACT_CHOICES,  
        widget= forms.Select(attrs={'class': 'form-select'}),
        required=True 
    )

    class Meta:
        model = Contacts
        fields = {
            'str_name',
            'email',
            'str_phone_number',
            'str_type_contact'
        }