from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import Contacts, Customer
from business.forms import ContactsForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

def parse_html_path(template_path,page):
    html_location = template_path + f'{page}.html'
    return html_location

CONTACT_PATH = 'business/Contact/'

@login_required
def new_contact(request, customer_id):
    try:
        customer_id = uncrip(customer_id)
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home_page')

    html_location = parse_html_path(CONTACT_PATH,'new_contact')

    if request.method == 'POST':
        form = ContactsForm(request.POST) 
        if form.is_valid():
            contact = form.save(commit=False)
            contact.customer = customer_instance
            contact.save()
            return redirect('profile_contact', crip(str(contact.contact_id)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = ContactsForm()
        html_location = parse_html_path(CONTACT_PATH,'new_contact')
        response_dict = { 'form': form}
        return render(request, html_location, response_dict)

@login_required   
def profile_contact(request, contact_id):
    contact_id = uncrip(contact_id)
    contact = get_object_or_404(Contacts, contact_id=contact_id)
    html_location = parse_html_path(CONTACT_PATH,'profile_contact')
    response_dict = {'contact': contact}
    return render(request, html_location, response_dict)

@login_required
def list_contacts(request):
    customer_id = request.user.customer.customer_id
    contacts = Contacts.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(CONTACT_PATH,'list_contacts')

    for contact in contacts: 
        contact.detail_url = reverse(
            'profile_contact',
            args=[crip(str(contact.contact_id))]
        )
        contact.save()

    response_dict = {
        'contacts': contacts,
        'new_contact': reverse('new_contact', args=[crip(str(customer_id))])
    }
    return render(request, html_location, response_dict)

@login_required
def list_contacts_by_id(request):
    contacts = Contacts.objects.all()
    html_location = parse_html_path(CONTACT_PATH,'list_contacts')

    for contact in contacts:
        contact.detail_url = reverse(
            'profile_contact',
            args=[crip(str(contact.contact_id))]
        )

        contact.save()

    response_dict = {
        'contacts': contacts
    }
    return render(request, html_location, response_dict)