from django.shortcuts import render, redirect
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
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
        self.authenticate_path = 'authenticate/'
        self.common_path = 'common/'
        self.template_path = 'business/CustomUser/'

    def parse_common_path(self,page):
        return self.common_path + f'{page}.html'
    
    def parse_authenticate_path(self,page):
        return self.authenticate_path + f'{page}.html'
    
    def parse_html_path(self,page):
        html_location = self.template_path + f'{page}.html'
        return html_location

    def render_add(self, request):
        form = CustomUserForm()
        html_location = self.parse_html_path('signup')
        dict_form = {
            'form': form
        }
        return render(request, html_location, dict_form)
    
    # def get_profiles(self, request):
    #     tables = User.objects.all()
    #     for table in tables:
    #         table.detail_url = reverse(
    #             'table_view', 
    #             args=[crip(str(table.id_table))]
    #         )
    #         table.save()
    #     html_location = self.parse_html_path('list')
    #     response_dict = {'tables': tables}
    #     return render(request, html_location, response_dict)
    
    def login(self,request):
        html_location = self.parse_html_path('login')
        response_dict = {

        }
        return render(request,html_location, response_dict)
    
    def home(self,request):
        html_location = self.parse_common_path('home')
        return render(request,html_location)

    def get_profile(self,request,username):
        try:
            custom_user = get_object_or_404(CustomUser, username=username)
            html_location = self.parse_html_path('profile')
            response_dict = {'user': custom_user}
            return render(request, html_location, response_dict)
        except Http404:
            return redirect('table_add')

    def get(self, request, argument=None):
        if request.path == '/':
            return self.home(request)
        elif request.path == '/signup/':
            return self.render_add(request)
        elif request.path == '/login/':
            return self.login(request)
        elif argument is not None:
            id_tabela = uncrip(argument)
            return self.get_profile(request,id_tabela)
        elif argument is None:
            return self.get_profiles(request)


    def post(self, request):
        form = CustomUserForm(request.POST)
        print(form)
        html_location = self.parse_html_path('signup')
        print(form.errors)
        if form.is_valid():
            print('valid')
            user = form.save()
            return redirect('user_profile', crip(str(user.username)))
        else:
            print('invalid')
            response_dict = {
                'form': form
            }
            return render(request, html_location, response_dict)


class CustomerView(View):
    def __init__(self):
        self.template_path = 'business/customer/'

    def parse_html_path(self,page):
        html_location = self.template_path + f'{page}.html'
        return html_location

    def add(self, request):
        form = CustomerForm()
        html_location = self.parse_html_path('add')
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
            company = get_object_or_404(Customer, id_customer=id_customer)
            html_location = self.parse_html_path('profile')
            response_dict = {'company': company}
            return render(request, html_location, response_dict)
        except Http404:
            return redirect('signup_company')
    
    def get(self, request, argument=None):
        if request.path == '/company/signup/':
            return self.add(request)
        elif argument is not None:
            id_customer = uncrip(argument)
            return self.get_profile(request,id_customer)
        elif argument is None:
            return self.get_profiles(request)
        else:
            return redirect('signup_company')

    def post(self, request):
        form = CustomerForm(request.POST)
        
        html_location = self.parse_html_path('signup')

        if form.is_valid():
            company = form.save()
            return redirect('view_company', company.id_company)
        else:
            response_dict = {'form': form}
            return render(request, html_location, response_dict)

    def put(self, request, id_company=None):
        company = get_object_or_404(Customer, id_company=id_company)
        form = CustomerForm(request.POST, instance=company)
        html_location = self.parse_html_path('profile')
        
        response_dict = {
            'companies': form
        }

        if form.is_valid():
            form.save()
            return redirect('details_company', id=id_company)
        return render(request, html_location, response_dict)