from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Tables
from business.models import Customer,DataSet
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

def new_table_by_id(request, dataset_id):
    try:
        dataset_id = uncrip(dataset_id)
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
        dataset_instance = DataSet.objects.get(dataset_id=dataset_id)
    except Customer.DoesNotExist:
        return redirect('home')
    print(customer_instance)
    if request.method == 'POST':
        form = TablesForm(request.POST)
        html_location = parse_html_path(TABLE_PATH,'add')
        if form.is_valid():
            table = form.save(commit=False)
            table.customer = customer_instance
            table.dataset = dataset_instance
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
        html_location = parse_html_path(TABLE_PATH,'add')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

def get_tables(request, table_id=None):
    customer_id = request.user.customer.customer_id
    tables = Tables.objects.filter(customer_id=customer_id)
    for table in tables:
        table.selected = False
        table.detail_url = reverse('view_tables_id',args=[crip(str(table.table_id))])
        table.save()

    if table_id == None:
        card_table = tables[0]
    else:
        card_table = Tables.objects.get(table_id=uncrip(table_id))

    html_location = parse_html_path(TABLE_PATH,'list')
    response_dict = {
        'tables': tables,
        'card_table': card_table
    }
    return render(request, html_location, response_dict)

def get_table(request,table_id):
    try:
        table_id = uncrip(table_id)
        table = get_object_or_404(Tables, table_id=table_id)
        html_location = parse_html_path(TABLE_PATH,'detail')
        response_dict = {
            # 'add': reverse('column_add',args=[crip(str(table.id_table))]),
            # 'look_all': reverse('columns_list',args=[crip(str(table.id_table))]),
            # 'exclude': reverse('column_add',args=[crip(str(table.id_table))]),
            'table': table
        }
        print(response_dict)
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('table_add')
