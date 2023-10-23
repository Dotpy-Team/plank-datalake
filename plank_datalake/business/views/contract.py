from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import Customer, Contract
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

def new_contract(request,id_customer):
    try:
        id_customer = uncrip(id_customer)
        customer_instance = Customer.objects.get(id_customer=id_customer)
    except Customer.DoesNotExist:
        # Lide com o caso em que o sistema não existe
        return redirect('home')
    
    if request.method == 'POST':
        form = ContractForm(request.POST)
        html_location = parse_html_path(CONTRACT_PATH,'new_contract')
        if form.is_valid():
            contract = form.save(commit=False)
            contract.id_customer = customer_instance
            contract.save()
            return redirect('profile_contract', crip(str(contract.id_contract)))
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

def  profile_contract(request,id_dataset):
    # try:
    id_dataset = uncrip(id_dataset)
    contract = get_object_or_404(Contract, id_dataset=id_dataset)
    html_location = parse_html_path(DATASET_PATH,'profile_dataset')
    response_dict = {
        'dataset': dataset,
        'new_table':reverse('new_table_by_id',args=[crip(str(dataset.id_dataset))])
    }
    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')