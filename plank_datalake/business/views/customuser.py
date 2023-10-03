from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import CustomUser
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

def home_page(request):
    html_location = parse_common_path('home')
    return render(request,html_location)

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
        response_dict = {
            'user': custom_user,
            'new_user': reverse('new_user',args=[crip(str(custom_user.id_customer))])
        }
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