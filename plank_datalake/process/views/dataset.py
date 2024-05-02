from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import Customer
from process.models import DataSet, System
from process.forms import DataSetForm
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
DATASET NEW_DATASET
DATASET PROFILE

"""
#######################################

DATASET_PATH = 'process/DataSet/'

@login_required
def new_dataset(request,system_id):
    try:
        system_id = uncrip(system_id)
        system_instance = System.objects.get(system_id=system_id)
    except System.DoesNotExist:
        # Lide com o caso em que o sistema não existe
        return redirect('home')
    
    if request.method == 'POST':
        form = DataSetForm(request.POST)
        html_location = parse_html_path(DATASET_PATH,'new_dataset')
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.system = system_instance
            dataset.save()

            return redirect('profile_dataset', crip(str(dataset.dataset_id)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = DataSetForm()
        html_location = parse_html_path(DATASET_PATH,'new_dataset')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

@login_required
def all_dataset(request):
    try:
        customer_id = request.user.customer.customer_id
        system = System.objects.filter(customer_id=customer_id)
        datasets = DataSet.objects.filter(system_id__in=system)
    except Customer.DoesNotExist:
        return redirect('home')
    html_location = parse_html_path(DATASET_PATH,'all_dataset')

    for dataset in datasets:
        dataset.detail_url = reverse('profile_dataset',args=[crip(str(dataset.dataset_id))])
        dataset.save()

    response_dict = {
        'datasets': datasets
    }
    return render(request, html_location, response_dict)

@login_required
def profile_dataset(request,dataset_id):
    # try:
    dataset_id = uncrip(dataset_id)
    dataset = get_object_or_404(DataSet, dataset_id=dataset_id)
    html_location = parse_html_path(DATASET_PATH,'profile_dataset')
    response_dict = {
        'dataset': dataset,
        'new_table':reverse('new_table_by_id',args=[crip(str(dataset.dataset_id))])
    }
    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')