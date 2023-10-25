from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import ContractItem, Contract
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

def new_contract_item(request,id_contract):
    try:
        id_contract = uncrip(id_contract)
        contract_instance = Contract.objects.get(id_contract=id_contract)
    except Contract.DoesNotExist:
        # Lide com o caso em que o sistema não existe
        return redirect('home')
    
    if request.method == 'POST':
        form = ContractItemForm(request.POST)
        html_location = parse_html_path(CONTRACTITEM_PATH,'new_contract_item')
        if form.is_valid():
            contractitem = form.save(commit=False)
            contractitem.id_contract = contract_instance
            contractitem.save()
            return redirect('profile_contract', crip(str(id_contract)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = ContractItemForm()
        html_location = parse_html_path(CONTRACTITEM_PATH,'new_contract_item')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)