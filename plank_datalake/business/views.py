from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from .models import Customer, CustomUser, Layer, System, DataSet, Task
from .forms import *
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text


common_path = 'common/'
CUSTOMUSER_PATH = 'business/CustomUser/'

def parse_common_path(page):
    return common_path + f'{page}.html'

def parse_html_path(template_path,page):
    html_location = template_path + f'{page}.html'
    return html_location

def home_page(request):
    html_location = parse_common_path('home')
    return render(request,html_location)

#######################################
"""
USER SIGNUP
USER PROFILE
USER LOGIN

"""
#######################################

def new_user(request, id_customer):
    id_customer = uncrip(id_customer)
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        html_location = parse_html_path(CUSTOMUSER_PATH,'signup')
        if form.is_valid():
            user = form.save()
            return redirect('user_profile', crip(str(user.email)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:
        form = CustomUserForm(
                initial={'id_customer': id_customer}
            )
        print(form)
        html_location = parse_html_path(CUSTOMUSER_PATH,'signup')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

def user_login(request, message=None):
    html_location = parse_html_path(CUSTOMUSER_PATH,'login')
    if message is not None:
        response_dict = {
            'error_message': message
        }
    else:
        response_dict = {}
    return render(request,html_location, response_dict)

def user_profile(request,email):
    email = uncrip(email)
    try:
        custom_user = get_object_or_404(CustomUser, email=email)
        html_location = parse_html_path(CUSTOMUSER_PATH,'profile')
        response_dict = {'user': custom_user}
        print(response_dict)
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('table_add')

def users_list_by_id_customer(request,id_customer):
    id_customer = uncrip(id_customer)
    users = CustomUser.objects.filter(id_customer=id_customer)
    html_location = parse_html_path(CUSTOMUSER_PATH,'list')
    for user in users:
        user.detail_url = reverse(
            'user_profile',
            args=[crip(str(user.email))]
        )
        
        user.save()

    response_dict = {
        'users': users
    }

    print(response_dict)
    return render(request, html_location, response_dict)


def all_users(request):
    users = CustomUser.objects.all()
    html_location = parse_html_path(CUSTOMUSER_PATH,'list')
    for user in users:
        user.detail_url = reverse(
            'user_profile',
            args=[crip(str(user.email))]
        )
        user.save()

    response_dict = {'users': users}
    return render(request, html_location, response_dict)

# def post_user_auth(request):
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     print(password)
#     user = authenticate(request, email=email, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('user_profile',crip(email))
#     else:
#         error_message = 'Credenciais inválidas. Por favor, tente novamente.'                
#         return get_login_page(request,message=error_message)
    

#######################################
"""
USER NEW_CUSTOMER
USER PROFILE
USER LOGIN

"""
#######################################

CUSTUMER_PATH = 'business/Customer/'

def new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        html_location = parse_html_path(CUSTUMER_PATH,'signup')

        if form.is_valid():
            company = form.save()
            return redirect('profile_customer', crip(str(company.id_customer)))
        else:
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = CustomerForm()
        html_location = parse_html_path(CUSTUMER_PATH,'signup')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

def list_customers(request):
    customers = Customer.objects.all()
    html_location = parse_html_path(CUSTUMER_PATH,'list')
    for customer in customers:
        customer.detail_url = reverse(
            'profile_customer',
            args=[crip(str(customer.id_customer))]
        )
        customer.save()

    response_dict = {'customers': customers}
    return render(request, html_location, response_dict)
    
def profile_customer(request,id_customer):
    id_customer = uncrip(id_customer)
    try:
        customer = get_object_or_404(Customer, id_customer=id_customer)
        html_location = parse_html_path(CUSTUMER_PATH,'profile')
        response_dict = {
            'customer': customer,
            'users':reverse('users_list_by_id_customer',args=[crip(str(customer.id_customer))]),
            'new_user': reverse('new_user',args=[crip(str(id_customer))]),
            'new_table': reverse('new_table',args=[crip(str(id_customer))]),
            'new_system': reverse('new_system',args=[crip(str(id_customer))]),
            'new_task': reverse('new_task',args=[crip(str(id_customer))]),
            'view_tables': reverse('view_tables',args=[crip(str(id_customer))]) 
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('signup_company')

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
    html_location = parse_html_path(SYSTEM_PATH,'profile_system')
    response_dict = {
        'system': system,
        'new_dataset':reverse('new_dataset',args=[crip(str(system.id_system))])
    }
    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')


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

#######################################
"""
TASK NEW_TASK
TASK PROFILE_TASK

"""
#######################################

TASK_PATH = 'business/Task/'

def new_task_by_id_customer(request,id_customer):
    id_customer = uncrip(id_customer)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        html_location = parse_html_path(TASK_PATH,'new_task')

        if form.is_valid():
            task = form.save()
            return redirect('profile_task', crip(str(task.id_task)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = TaskForm(
            initial={
                'id_customer': id_customer,
                'id_table':0})
        html_location = parse_html_path(TASK_PATH,'new_task')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

def profile_task(request,id_task):
    id_task = uncrip(id_task)
    # try:
    task = get_object_or_404(Task, id_task=id_task)
    html_location = parse_html_path(TASK_PATH,'profile_task')
    response_dict = {
        'task': task
    }
    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')
