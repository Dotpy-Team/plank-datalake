from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import ContractItem, Contract, Service
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
def new_contract_item(request,contract_id):
    try:
        customer_id = request.user.customer.customer_id
        contract_id = uncrip(contract_id)
        contract_instance = Contract.objects.get(contract_id=contract_id)
    except Contract.DoesNotExist:
        return redirect('home')
    
    if request.method == 'POST':
        form = ContractItemForm(request.POST)
        
        try:
            service_id = request.POST.get('service_id')
            service_instance = Service.objects.get(service_id=service_id)
        except Service.DoesNotExist:
            return redirect('home')

        html_location = parse_html_path(CONTRACTITEM_PATH,'new_contract_item')

        if form.is_valid():
            contractitem = form.save(commit=False)
            contractitem.contract = contract_instance
            contractitem.service = service_instance
            contractitem.save()
            return redirect('profile_contract', crip(str(contract_id)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = ContractItemForm()

        form.fields['service'].queryset = Service.objects.filter(customer_id=customer_id)
        form.fields['service'].widget.attrs['class'] = 'form-select'
        form.fields['service'].label = 'service'

        html_location = parse_html_path(CONTRACTITEM_PATH,'new_contract_item')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)