from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Tables, Step, Pipeline
from business.models import Customer
from process.forms import StepForm, TablesFormStep
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

STEP_PATH = 'process/Step/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location


def new_step(request):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = get_object_or_404(Customer, customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    form = StepForm(request.POST)
    html_location = parse_html_path(STEP_PATH, 'new_step')

    if request.method == 'POST':
        if form.is_valid():
            step = form.save(commit=False)
            step.customer = customer_instance
            step.save()
            return redirect('new_child_table', crip(str(step.step_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'   
            error_dict = {
                'form': form,
                'error_message': error_message,
                'errors': form.errors
            }
            return render (request, html_location, error_dict)
    else:
        form = StepForm()
        response_dict = { 'form': form }
        return render(request, html_location, response_dict)

#def new_child_table(request):

def detail_step(request):
    pass

def list_step(request):
    pass 


