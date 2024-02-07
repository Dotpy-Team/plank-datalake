from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Conector 
from business.models import Customer
from process.forms import SheetConfigForm, PostConfigForm
import json
import base64


def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip


def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text


CONFIG_PATH = 'process/TableConfig/'


def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location

@login_required
def new_conector(request):
    html_location = parse_html_path(CONFIG_PATH, 'landing')
    return render(request, html_location)

@login_required
def new_sheets_table(request): 
    try: 
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    html_location = parse_html_path(CONFIG_PATH, 'new_conector')

    if request.method == 'POST':
        form = SheetConfigForm(request.POST)
        
        if form.is_valid():
            conector = form.save(commit=False)
            conector.customer = customer_instance
            conector.save()
            return redirect('conector_detail', crip(str(conector.conector_id)))
        else: 
            error_message = 'Os valores estão incorretos, tente novamnete'
            error_dict ={
                'form': form,  
                'error_message':error_message,
                'form_error': form.errors
            }
            return render(request, html_location, error_dict)
    else: 
        form = SheetConfigForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)
    
@login_required
def new_postgree_table(request): 

    try: 
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')

    html_location = parse_html_path(CONFIG_PATH, 'new_conector') 

    if request.method  == 'POST':
        form = PostConfigForm(request.POST)

        if form.is_valid():
            conector = form.save(commit=False)
            conector.customer = customer_instance
            conector.save()
            return redirect('conector_detail', crip(str(conector.conector_id)))
        
        else:
            error_message = 'Os valores estão incorretos, tente novamnete'
            error_dict = {
                'form': form,
                'error_message': error_message,
                'error_form': form.errors 
            }
            return render(request, html_location, error_dict)
    else:
        form = PostConfigForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)

@login_required
def conector_detail(request, conector_id):
    conector_id = uncrip(conector_id)

    conector = get_object_or_404(Conector, conector_id=conector_id)
    html_location = parse_html_path(CONFIG_PATH, 'conector_detail')
    response_dict = {
        'conector': conector
    }

    return render(request, html_location, response_dict) 

@login_required
def conector_list(request):

    try:
        customer_id = request.user.customer.customer_id
        customer_instance = get_object_or_404(Customer, customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    conectors  = Conector.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(CONFIG_PATH, 'list_conector')

    for conector in conectors:
        conector.detail_url = reverse(
            'conector_detail',
            args=[crip(str(conector.conector_id))]
        )

        conector.save()
    
    response_dict = {
        'conectors': conectors
    }

    return render(request, html_location, response_dict)