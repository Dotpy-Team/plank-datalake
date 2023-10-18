from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import System, DataSet
from business.forms import SystemForm
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
SYSTEM NEW_SYSTEM
SYSTEM PROFILE

"""
#######################################

SYSTEM_PATH = 'business/System/'

def new_system(request,id_customer):
    id_customer = uncrip(id_customer)
    if request.method == 'POST':
        form = SystemForm(request.POST)
        html_location = parse_html_path(SYSTEM_PATH,'new_system')

        if form.is_valid():
            system = form.save()
            return redirect('profile_system', crip(str(system.id_system)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = SystemForm(initial={'id_customer': id_customer})
        html_location = parse_html_path(SYSTEM_PATH,'new_system')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

def profile_system(request,id_system):
    id_system = uncrip(id_system)
    # try:
    system = get_object_or_404(System, id_system=id_system)
    datasets = DataSet.objects.filter(id_system=id_system)

    for dataset in datasets:
        dataset.detail_url = reverse(
            'profile_dataset',
            args=[crip(str(dataset.id_dataset))]
        )
        dataset.save()

    html_location = parse_html_path(SYSTEM_PATH,'profile_system')
    response_dict = {
        'system': system,
        'datasets':datasets,
        'new_dataset':reverse('new_dataset',args=[crip(str(system.id_system))])
    }

    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')

def list_system(request):
    systems = System.objects.all()
    html_location = parse_html_path(SYSTEM_PATH,'list_system')
    for system in systems:
        system.detail_url = reverse(
            'profile_system',
            args=[crip(str(system.id_system))]
        )
        system.save()
    response_dict = {'systems': systems}
    
    return render(request, html_location, response_dict)