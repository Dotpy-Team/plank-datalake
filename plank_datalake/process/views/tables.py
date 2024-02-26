from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Tables, RaciActivity, Columns
from business.models import Customer,DataSet, System
from process.forms import TablesForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

TABLE_PATH = 'process/Tables/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location

@login_required
def new_table_by_id(request, dataset_id):
    try:
        dataset_id = uncrip(dataset_id)
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
        dataset_instance = DataSet.objects.get(dataset_id=dataset_id)
    except Customer.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        form = TablesForm(request.POST)
        html_location = parse_html_path(TABLE_PATH,'add')
        if form.is_valid():
            table = form.save(commit=False)
            table.customer = customer_instance
            table.dataset = dataset_instance
            table.layer = 'ingestion'
            table.save()
            return redirect('table_view', crip(str(table.table_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:
        form = TablesForm()

        form.fields['raci_activity'].queryset = RaciActivity.objects.filter(customer_id=customer_id)
        form.fields['raci_activity'].widget.attrs['class'] = 'form-select'
        form.fields['raci_activity'].label = 'RACI'
        
        html_location = parse_html_path(TABLE_PATH,'add')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

@login_required
def get_tables(request, table_id=None):
    customer_id = request.user.customer.customer_id
    tables = Tables.objects.filter(customer_id=customer_id)
    for table in tables:
        table.selected = False
        table.detail_url = reverse('view_tables_id',args=[crip(str(table.table_id))])
        table.save()
    if len(tables) > 0:
        if table_id == None:
            card_table = tables[0]
            card_table.details_url = reverse('table_view',args=[crip(str(card_table.table_id))])
        else:
            card_table = Tables.objects.get(table_id=uncrip(table_id))
            card_table.details_url = reverse('table_view',args=[crip(str(card_table.table_id))])
    else:
        card_table = None

    html_location = parse_html_path(TABLE_PATH,'list')
    response_dict = {
        'tables': tables,
        'card_table': card_table
    }
    return render(request, html_location, response_dict)

@login_required
def get_table(request,table_id):
    try:
        table_id = uncrip(table_id)
        table = Tables.objects.get(table_id=table_id)
        columns = Columns.objects.filter(table_id=table_id)
        html_location = parse_html_path(TABLE_PATH,'detail')
        response_dict = {
            'add': reverse('new_column',args=[crip(str(table.table_id))]),
            'new_job': reverse('new_execution',args=[crip(str(table.table_id))]),
            'view_job': reverse('detail_execution', args=[crip(str(table.table_id))]),
            'new_dependencie': reverse('new_dependencies', args=[crip(str(table.table_id))]),
            'columns': columns,
            'table': table
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('table_add')
