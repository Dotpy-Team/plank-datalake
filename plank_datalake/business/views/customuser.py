from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q 
from business.models import CustomUser, Customer
from process.models import RaciActivity, RaciRelated
from business.forms import CustomUserForm
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

@login_required
def home_page(request):
    html_location = parse_common_path('home')
    print(request.user)
    return render(request,html_location)

@login_required
def new_user(request, customer_id):
    try:
        customer_id = uncrip(customer_id)
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        # Lide com o caso em que o sistema não existe
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        html_location = parse_html_path(CUSTOMUSER_PATH,'signup')
        if form.is_valid():
            user = form.save(commit=False)
            user.customer = customer_instance
            user.save()
            return redirect('admin_user_profile', crip(str(user.email)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:
        form = CustomUserForm()
        
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
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            response_dict['errors'] = 'Credenciais inválidas. Por favor, tente novamente.'
    
    return render(request,html_location, response_dict)

@login_required
def user_profile(request):
    email = request.user.email
    user_id = request.user.id
  
    related = RaciRelated.objects.filter(person=user_id)  
    list_related = []

    for aux_related in related:
        list_related.append(aux_related.activity_id)

    activities = RaciActivity.objects.filter(Q(responsible=user_id) | Q(accountable=user_id) | Q(activity_id__in = list_related))

    for aux_activity in activities:
        if aux_activity.accountable_id == user_id:
            aux_activity.str_type = 'Aprovador' 
        elif aux_activity.responsible_id == user_id:
            aux_activity.str_type = 'Responsável'
        else:
            aux_related = related.filter(activity=aux_activity.activity_id)

            for aux in aux_related:
                if aux.str_type == "CON":
                    aux.str_type = 'Consultado'
                elif aux.str_type == "INF":
                    aux.str_type = 'Informado'

            aux_activity.str_type = aux.str_type


    try:
        custom_user = get_object_or_404(CustomUser, email=email)
        html_location = parse_html_path(CUSTOMUSER_PATH,'profile')
        response_dict = {
            'user': custom_user,
            'activities': activities,
            'new_user': reverse('new_user',args=[crip(str(custom_user.customer_id))])
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('table_add')

@login_required
def admin_user_profile(request,email):
    email = uncrip(email)

    print(request.user.is_staff)
    print(request.user.is_superuser)
    try:
        custom_user = get_object_or_404(CustomUser, email=email)
        html_location = parse_html_path(CUSTOMUSER_PATH,'admin_profile')
        response_dict = {
            'custom_user': custom_user,
            'new_user': reverse('new_user',args=[crip(str(custom_user.customer_id))])
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('table_add')

@login_required
def users_list_by_id_customer(request,customer_id):
    customer_id = uncrip(customer_id)
    users = CustomUser.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(CUSTOMUSER_PATH,'list')
    for user in users:
        user.detail_url = reverse(
            'admin_user_profile',
            args=[crip(str(user.email))]
        )
        user.save()

    response_dict = {
        'users': users,
        'new_user': reverse('new_user',args=[crip(str(customer_id))])
    }
    return render(request, html_location, response_dict)

@login_required
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

@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home_page')
