from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import ContractItem, Contract, Service, Customer
from business.forms import ContractItemForm
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

#######################################

"""
ContractItem NEW_DATASET
ContractItem PROFILE

"""

#######################################

CONTRACTITEM_PATH = 'business/ContractItem/'

@login_required
def new_contract_item(request, contract_id):
    try:
        contract_id = uncrip(contract_id)
        contract_instance = Contract.objects.get(contract_id=contract_id)
        customer_id = contract_instance.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Contract.DoesNotExist:
        return redirect('home_page')
    
    html_location = parse_html_path(CONTRACTITEM_PATH, 'new_contract_item')

    if request.method == 'POST':

        form = ContractItemForm(request.POST)

        form.fields['service'].queryset = Service.objects.all()
        form.fields['service'].widget.attrs['class'] = 'form-select'
        form.fields['service'].label = 'service'

        try:
            service_id = request.POST.get('service')
            service_instance = Service.objects.get(service_id=service_id)
        except Service.DoesNotExist:
            return redirect('home_page')
        
        if form.is_valid():
            item = form.save(commit=False)
            item.contract = contract_instance
            item.customer = customer_instance
            item.service = service_instance
            item.save()
            return redirect('profile_contract', crip(str(contract_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                "form": form,
                "error_message": error_message,
                "error_forms": form.errors
            }
            return render(request, html_location, response_dict)
    else:
        form = ContractItemForm()

        form.fields['service'].queryset = Service.objects.filter()
        form.fields['service'].widget.attrs['class'] = 'form-select'
        form.fields['service'].label = 'service'

        response_dict ={
            "form": form
        }

        return render(request, html_location, response_dict)
