from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.views import View
from business.models import Customer
from process.models import Trigger
from process.forms import TriggerForm
import base64


def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

TRIGGER_PATH = 'process/Trigger/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location

@login_required
def add_trigger(request):

    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    html_location = parse_html_path(TRIGGER_PATH, 'add')

    if request.method == 'POST':

        form = TriggerForm(request.POST)

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
        form = TriggerForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)

@login_required
def detail_trigger(request, trigger_id):

    trigger_id = uncrip(trigger_id)

    trigger = get_object_or_404(Trigger, trigger_id=trigger_id)
    html_location = parse_html_path(TRIGGER_PATH, 'detail')
    response_dict = {
        'trigger': trigger
    }

    return render(request, html_location, response_dict)

@login_required
def list_trigger(request):
    customer_id = request.user.customer.customer_id
    
    triggers = Trigger.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(TRIGGER_PATH, 'list')

    for trigger in triggers:
        trigger.detail_url = reverse(
            'detail_trigger',
            args=[crip(str(trigger.trigger_id))]
        )

        trigger.save()
    
    response_dict = {
        'triggers': triggers
    }

    return render(request, html_location, response_dict)