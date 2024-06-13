from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import Customer
from process.models import System, DataSet
from process.forms import SystemForm, GoogleSheetSystemForm, PostGreSytemForm, MySqlSystemForm, SQLiteSystemForm
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

SYSTEM_PATH = 'process/System/'

@login_required
def route(request):
    html_location = parse_html_path(SYSTEM_PATH, 'route')
    return render(request, html_location)

@login_required
def new_system(request):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        # Lide com o caso em que o sistema não existe
        return redirect('home')
    
    if request.method == 'POST':
        form = SystemForm(request.POST)
        html_location = parse_html_path(SYSTEM_PATH,'new_system')

        if form.is_valid():
            system = form.save(commit=False)
            system.str_table_type = 'system'
            system.customer = customer_instance
            system.save()
            return redirect('profile_system', crip(str(system.system_id)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = SystemForm(initial={'customer_id': customer_id})
        html_location = parse_html_path(SYSTEM_PATH,'new_system')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

@login_required
def profile_system(request,system_id):
    system_id = uncrip(system_id)
    system = get_object_or_404(System, system_id=system_id)
    system.img_path = f"images/{system.str_system_type}.png"
    datasets = DataSet.objects.filter(system_id=system_id)
    
    search = request.GET.get('search')

    if search:
        datasets = DataSet.objects.filter(str_title__icontains=search)
    
    datasets = datasets.order_by('dataset_id')

    paginator = Paginator(datasets, 6)  # 10 datasets por página
    page = request.GET.get('page')
    
    try:
        datasets = paginator.page(page)
    except PageNotAnInteger:
        datasets = paginator.page(1)
    except EmptyPage:
        datasets = paginator.page(paginator.num_pages)

    for dataset in datasets:
        dataset.detail_url = reverse(
            'profile_dataset',
            args=[crip(str(dataset.dataset_id))]
        )
        dataset.save()

    html_location = parse_html_path(SYSTEM_PATH,'profile_system')
    response_dict = {
        'system': system,
        'datasets':datasets,
        'new_dataset':reverse('new_dataset',args=[crip(str(system.system_id))]),
        'profile_system':reverse('profile_system',args=[crip(str(system.system_id))]),
        'search':search
    }

    return render(request, html_location, response_dict)

@login_required
def list_system(request):
    customer_id = request.user.customer.customer_id
    systems = System.objects.filter(customer_id=customer_id).order_by('system_id')

    html_location = parse_html_path(SYSTEM_PATH,'list_system')

    # Configuração da paginação
    paginator = Paginator(systems, 6)  # 10 sistemas por página
    page = request.GET.get('page')

    try:
        systems = paginator.page(page)
    except PageNotAnInteger:
        systems = paginator.page(1)
    except EmptyPage:
        systems = paginator.page(paginator.num_pages)
    

    for system in systems:
        system.detail_url = reverse(
            'profile_system',
            args=[crip(str(system.system_id))]
        )
        system.save()
        
    response_dict = {
        'systems': systems
    }
    
    return render(request, html_location, response_dict)

@login_required
def new_system_id(request,customer_id):
    customer_id = uncrip(customer_id)
    if request.method == 'POST':
        form = SystemForm(request.POST)
        html_location = parse_html_path(SYSTEM_PATH,'new_system')

        if form.is_valid():
            system = form.save()
            return redirect('profile_system', crip(str(system.system_id)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = SystemForm(initial={'customer_id': customer_id})
        html_location = parse_html_path(SYSTEM_PATH,'new_system')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)


@login_required
def new_sheets_system(request):
    try:
        customer_id = request.user.customer.customer_id 
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    html_location = parse_html_path(SYSTEM_PATH, 'new_sheets_system')

    if request.method == 'POST':
        
        form =  GoogleSheetSystemForm(request.POST)

        if form.is_valid():
            system = form.save(commit=False)
            system.str_system_type = 'google_sheets'
            system.customer =customer_instance
            system.save()
            return redirect('profile_system', crip(str(system.system_id)))
        else:
            error_message = 'Os valores estão incorretos, tente novamente'
            error_dict = {
                'form': form,
                'error_message': error_message,
                'form_error': form.errors 
            }
            return render(request, html_location, error_dict)
    else:
        form = GoogleSheetSystemForm()
        response_dict = {
            'form': form 
        }
        return render(request, html_location, response_dict)
    
@login_required 
def new_postgre_system(request):

    try:
        customer_id = request.user.customer.customer_id 
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    html_location = parse_html_path(SYSTEM_PATH, 'new_postgre_system')

    if request.method == 'POST':

        form = PostGreSytemForm(request.POST)

        if form.is_valid():
            system = form.save(commit=False)
            system.str_system_type = 'postgre'
            system.customer = customer_instance 
            system.save()
            return redirect('profile_system', crip(str(system.system_id)))
        else:
            error_message = 'Os valores estão incorretos, tente novamente'
            error_dict = {
                'form': form,
                'error_message': error_message,
                'form_error': form.errors
            }
            return render(request, html_location, error_dict)
    else:
        form = PostGreSytemForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)

@login_required
def new_mysql_system(request): 

    try: 
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    html_location = parse_html_path(SYSTEM_PATH, 'new_mysql_system')

    if request.method == 'POST':

        form = MySqlSystemForm(request.POST)

        if form.is_valid():
            system = form.save(commit=False)
            system.str_system_type = 'mysql'
            system.customer = customer_instance
            system.save()
            return redirect('profile_system', crip(str(system.system_id)))
        else:
            error_message = 'Os valores estão incorretos, tente novamente'
            error_dict = {
                'form': form,
                'error_message': error_message,
                'form_error': form.errors
            }
            return render(request, html_location, error_dict)
    else:
        form = MySqlSystemForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)
    
@login_required
def new_sqlite_system(request):

    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    html_location = parse_html_path(SYSTEM_PATH, 'new_sqlite_system')

    if request.method == 'POST':

        form = SQLiteSystemForm(request.POST)

        if form.is_valid():
            system = form.save(commit=False)
            system.str_system_type = 'sqlite'
            system.customer = customer_instance
            system.save()
            return redirect('profile_system', crip(str(system.system_id)))
        else:
            error_message = 'Os valores estão incorretos, tente novamente'
            error_dict = {
                'form': form,
                'error_message': error_message,
                'form_error': form.errors
            }
            return render(request, html_location, error_dict)
    else:
        form = SQLiteSystemForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)

@login_required
def admin_list_system(request):
    systems = System.objects.all()
    html_location = parse_html_path(SYSTEM_PATH,'list_system')
    for system in systems:
        system.detail_url = reverse(
            'profile_system',
            args=[crip(str(system.system_id))]
        )
        system.save()
    response_dict = {'systems': systems}
    
    return render(request, html_location, response_dict)

