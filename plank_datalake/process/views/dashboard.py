from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from business.models import Customer,Contract, Contacts
from process.models import Dashboard
from process.forms import DashboardForm
import base64

DASHBOARD_PATH = 'process/Dashboard/'

def parse_html_path(template_path,page):
    html_location = template_path + f'{page}.html'
    return html_location

@login_required


def dashboard(request):
    try:
        html_location = parse_html_path(DASHBOARD_PATH,'dashboard')
        dashboards = Dashboard.objects.all()
        response_dict = {
            'dashboards':dashboards
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('home')

def list_dashboard(request):
    try:
        html_location = parse_html_path(DASHBOARD_PATH,'list_dash')
        dashboards = Dashboard.objects.all()
        response_dict = {
            'dashboards':dashboards
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('home')
    
@login_required
def add_dashboard(request):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    html_location = parse_html_path(DASHBOARD_PATH, 'new_dash')

    if request.method == 'POST':

        form = DashboardForm(request.POST)

        if form.is_valid():
            trigger = form.save(commit=False)
            trigger.customer = customer_instance
            trigger.save()
            return redirect('detail_trigger', crip(str(trigger.trigger_id)))
        else: 
            error_message = 'Informações da trigger estão inválidas'
            error_dict = {
                'form': form,
                'error_message': error_message,
                'errors': form.errors
            }
            return render(request, html_location, error_dict)
    else: 
        form = DashboardForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)