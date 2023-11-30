from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import Customer, Contract, ContractItem, Service
from business.forms import ContractForm
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
Contract NEW_DATASET
Contract PROFILE

"""
#######################################

CONTRACT_PATH = 'business/Contract/'

def new_contract(request,customer_id):
    try:
        customer_id = uncrip(customer_id)
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        # Lide com o caso em que o sistema não existe
        return redirect('home')
    
    if request.method == 'POST':
        form = ContractForm(request.POST)
        html_location = parse_html_path(CONTRACT_PATH,'new_contract')
        if form.is_valid():
            contract = form.save(commit=False)
            contract.customer_id = customer_instance
            contract.save()
            return redirect('profile_contract', crip(str(contract.contract_id)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = ContractForm()
        html_location = parse_html_path(CONTRACT_PATH,'new_contract')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

def  profile_contract(request,contract_id):
    # try:
    contract_id = uncrip(contract_id)
    contract = get_object_or_404(Contract, contract_id=contract_id)
    contract_item = ContractItem.objects.select_related('contractitem__service').filter(contract_id=contract_id)

    html_location = parse_html_path(CONTRACT_PATH,'profile_contract')
    response_dict = {
        'contract': contract,
        'contractitem': contract_item,
        'new_contract_item':reverse('new_contract_item',args=[crip(str(contract.contract_id))])
    }
    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')

def admin_list_contracts(request):
    contracts = Contract.objects.all()
    html_location = parse_html_path(CONTRACT_PATH,'list_contract')
    for contract in contracts:
        contract.detail_url = reverse(
            'profile_contract',
            args=[crip(str(contract.contract_id))]
        )
        contract.save()

    response_dict = {'contracts': contracts}
    return render(request, html_location, response_dict)