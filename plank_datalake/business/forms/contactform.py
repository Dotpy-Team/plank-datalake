from django import forms 
from business.models import Contacts


class ContactsForm(forms.ModelForm):
    str_first_name = forms.CharField(
        label='Nome', 
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_last_name = forms.CharField(
        label='Sobrenome',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
    )

    str_email = forms.CharField(
        label='E-mail',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    
    str_comercial_email = forms.CharField(
        label='E-mail Comercial',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= False
    )

    str_phone_number = forms.CharField(
        label = 'Telefone',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    str_comercial_phone_number = forms.CharField(
        label='Telefone Comercial',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    str_whatsapp_number = forms.CharField(
        label='WhatsApp',
        widget= forms.TextInput(attrs={'class': 'form-control'}),
        required= True
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
            'str_first_name',
            'str_last_name', 
            'str_email',
            'str_comercial_email',
            'str_phone_number',
            'str_comercial_phone_number',
            'str_whatsapp_number',
            'str_type_contact'
        }