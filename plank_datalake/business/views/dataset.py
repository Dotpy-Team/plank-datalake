from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import DataSet
from business.forms import DataSetForm
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

DATASET_PATH = 'business/DataSet/'

def new_dataset(request,id_system):
    id_system = uncrip(id_system)
    if request.method == 'POST':
        form = DataSetForm(request.POST)
        html_location = parse_html_path(DATASET_PATH,'new_dataset')
        print(form.errors)
        if form.is_valid():
            dataset = form.save()
            return redirect('profile_dataset', crip(str(dataset.id_dataset)))
        else:
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = DataSetForm(initial={'id_system': id_system})
        html_location = parse_html_path(DATASET_PATH,'new_dataset')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

def profile_dataset(request,id_dataset):
    id_dataset = uncrip(id_dataset)
    # try:
    dataset = get_object_or_404(DataSet, id_dataset=id_dataset)
    html_location = parse_html_path(DATASET_PATH,'profile_dataset')
    response_dict = {
        'dataset': dataset,
        'new_dataset':reverse('new_dataset',args=[crip(str(dataset.id_system))])
    }
    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')