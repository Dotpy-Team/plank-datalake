from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.views import View
from .models import CustomUser,Customer
from .forms import CustomUserForm, CustomerForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

class CustomUserView(View):
    def __init__(self):
        self.common_path = 'common/'
        self.template_path = 'business/CustomUser/'

    def parse_common_path(self,page):
        return self.common_path + f'{page}.html'

    def parse_html_path(self,page):
        html_location = self.template_path + f'{page}.html'
        return html_location

    def get_signup(self, request):
        form = CustomUserForm()
        html_location = self.parse_html_path('signup')
        dict_form = {
            'form': form
        }
        return render(request, html_location, dict_form)
    
    def get_login_page(self, request, message=None):
        html_location = self.parse_html_path('login')
        if message is not None:
            response_dict = {'error_message': message}
        else:
            response_dict = {}
        return render(request,html_location, response_dict)

    def get_homepage(self,request):
        html_location = self.parse_common_path('home')
        return render(request,html_location)

    def get_profile(self,request,username):
        try:
            custom_user = get_object_or_404(CustomUser, username=username)
            html_location = self.parse_html_path('profile')
            response_dict = {'user': custom_user}
            print(response_dict)
            return render(request, html_location, response_dict)
        except Http404:
            return redirect('table_add')

    def post_user_auth(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile',crip(username))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'                
            return self.get_login_page(request,message=error_message)
        
    def post_create_user(self,request):
        form = CustomUserForm(request.POST)            
        html_location = self.parse_html_path('signup')
        
        if form.is_valid():
            user = form.save()
            return redirect('user_profile', crip(str(user.username)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors

            }
            return render(request, html_location, response_dict)

    def get(self, request, argument=None):
        if request.path == '/':
            return self.get_homepage(request)
        elif request.path == '/signup/':
            return self.get_signup(request)
        elif request.path == '/login/':
            return self.get_login_page(request)
        elif argument is not None:
            id_tabela = uncrip(argument)
            return self.get_profile(request,id_tabela)

    def post(self, request):
        #if access is login page, render with.
        if request.path == '/login/':
            return self.post_user_auth(request)
        #else, is a created user.
        else:
            return self.post_create_user(request)


class CustomerView(View):
    def __init__(self):
        self.template_path = 'business/Customer/'

    def parse_html_path(self,page):
        html_location = self.template_path + f'{page}.html'
        return html_location

    def signup(self, request):
        form = CustomerForm()
        html_location = self.parse_html_path('signup')
        dict_form = {
            'form': form
        }
        return render(request, html_location, dict_form)
    
    # @login_required
    def get_profiles(self, request):
        company = Customer.objects.all()
        html_location = self.parse_html_path('list_profiles')
        response_dict = {'companies': company}
        return render(request, html_location, response_dict)
    
    # @login_required
    def get_profile(self,request,id_customer):
        try:
            customer = get_object_or_404(Customer, id_customer=id_customer)
            html_location = self.parse_html_path('profile')
            response_dict = {'customer': customer}
            return render(request, html_location, response_dict)
        except Http404:
            return redirect('signup_company')
    
    def get(self, request, argument=None):
        print(request)
        if request.path == '/customer/':
            return self.signup(request)
        
        elif argument is not None:
            id_customer = uncrip(argument)
            return self.get_profile(request,id_customer)
        
        elif argument is None:
            return self.get_profiles(request)
                
        else:
            return redirect('signup_company')

    def post(self, request):
        form = CustomerForm(request.POST)
        print(form.errors)
        
        html_location = self.parse_html_path('signup')

        if form.is_valid():
            company = form.save()
            return redirect('profile_customer', crip(str(company.id_customer)))
        else:
            response_dict = {'form': form}
            return render(request, html_location, response_dict)

    def put(self, request, id_customer=None):
        company = get_object_or_404(Customer, id_customer=id_customer)
        form = CustomerForm(request.POST, instance=company)
        html_location = self.parse_html_path('profile')
        
        response_dict = {
            'companies': form
        }

        if form.is_valid():
            form.save()
            return redirect('details_company', id=id_customer)
        return render(request, html_location, response_dict)