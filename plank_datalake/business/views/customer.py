from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from business.models import Customer
from business.forms import CustomerForm
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

CUSTUMER_PATH = 'business/Customer/'

def new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        html_location = parse_html_path(CUSTUMER_PATH,'signup')
        print(form.errors)

        if form.is_valid():
            company = form.save()
            return redirect('admin_profile_customer', crip(str(company.id_customer)))
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

def admin_list_customers(request):
    customers = Customer.objects.all()
    html_location = parse_html_path(CUSTUMER_PATH,'list')
    for customer in customers:
        customer.detail_url = reverse(
            'admin_profile_customer',
            args=[crip(str(customer.id_customer))]
        )
        customer.save()

    response_dict = {'customers': customers}
    return render(request, html_location, response_dict)

def admin_profile_customer(request,id_customer):
    try:
        id_customer = uncrip(id_customer)
        customer = get_object_or_404(Customer, id_customer=id_customer)
        html_location = parse_html_path(CUSTUMER_PATH,'profile')
        response_dict = {
            'customer': customer,
            'users':reverse('users_list_by_id_customer',args=[crip(str(customer.id_customer))]),
            'new_user': reverse('new_user',args=[crip(str(id_customer))]),
            'new_table': reverse('new_table_by_id',args=[crip(str(id_customer))]),
            'new_system': reverse('new_system',args=[crip(str(id_customer))]),
            'new_task': reverse('new_task',args=[crip(str(id_customer))]),
            # 'view_tables': reverse('view_tables',args=[crip(str(id_customer))])
            'new_contract': reverse('new_contract',args=[crip(str(id_customer))])
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('new_customer')

# @login_required(login_url='user_login')
def profile_customer(request):
    try:
        id_customer = request.user.id_customer.id_customer
        customer = get_object_or_404(Customer, id_customer=id_customer)
        print(customer)
        html_location = parse_html_path(CUSTUMER_PATH,'profile')
        response_dict = {
            'customer': customer,
            # 'users':reverse('users_list_by_id_customer',args=[crip(str(customer.id_customer))]),
            # 'new_user': reverse('new_user',args=[crip(str(id_customer))]),
            # 'new_table': reverse('new_table_by_id',args=[crip(str(id_customer))]),
            # 'new_system': reverse('new_system',args=[crip(str(id_customer))]),
            # 'new_task': reverse('new_task',args=[crip(str(id_customer))]),
            # 'view_tables': reverse('view_tables',args=[crip(str(id_customer))]) 
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('new_customer')