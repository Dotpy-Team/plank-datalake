from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from business.models import Customer,Contract, Contacts
from business.forms import CustomerForm
import base64

DASHBOARD_PATH = 'process/Dashboard/'

def parse_html_path(template_path,page):
    html_location = template_path + f'{page}.html'
    return html_location

@login_required
def dashboard(request):
    try:
        html_location = parse_html_path(DASHBOARD_PATH,'dashboard')
        response_dict = {
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('home')