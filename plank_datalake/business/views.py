from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import CustomUser,Customer
from .forms import CustomUserForm, CustomerForm
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

    response_dict = {'users': users}
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

def customers_list(request):
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
    
def customer_profile(request,id_customer):
    id_customer = uncrip(id_customer)
    try:
        customer = get_object_or_404(Customer, id_customer=id_customer)
        html_location = parse_html_path(CUSTUMER_PATH,'profile')
        response_dict = {
            'customer': customer,
            'users':reverse(
                'users_list_by_id_customer',
                args=[crip(str(customer.id_customer))]
            )
        
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('signup_company')


# def put(self, request, id_customer=None):
#     company = get_object_or_404(Customer, id_customer=id_customer)
#     form = CustomerForm(request.POST, instance=company)
#     html_location = self.parse_html_path('profile')
    
#     response_dict = {
#         'companies': form
#     }

#     if form.is_valid():
#         form.save()
#         return redirect('details_company', id=id_customer)
#     return render(request, html_location, response_dict)