from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Tables, RaciActivity
from business.models import Customer,DataSet
from process.forms import ColumnsForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

TABLE_PATH = 'process/Columns/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location

@login_required
def new_column(request, table_id):
    try:
        table_id = uncrip(table_id)
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
        table_instance = Tables.objects.get(table_id=table_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    if request.method == 'POST':
        form = ColumnsForm(request.POST)
        html_location = parse_html_path(TABLE_PATH,'add')
        if form.is_valid():
            column = form.save(commit=False)
            column.customer = customer_instance
            column.table = table_instance
            column.save()
            return redirect('table_view', crip(str(column.table_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:
        form = ColumnsForm()

        html_location = parse_html_path(TABLE_PATH,'add')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)
