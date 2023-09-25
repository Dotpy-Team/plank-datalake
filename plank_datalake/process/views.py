from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.views import View
from .models import Tables
from .forms import TablesForm
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

def new_table(request):
    form = TablesForm()
    html_location = parse_html_path(TABLE_PATH,'add')

    dict_form = {
        'form': form
    }
    return render(request, html_location, dict_form)

def get_tables(request, id_table=None):
    tables = Tables.objects.all()
    for table in tables:
        if id_table == str(table.id_table):
            table.selected = True
        else:
            table.selected = False

        table.detail_url = reverse(
            'table_view', 
            args=[crip(str(table.id_table))]
        )
        table.save()

    if id_table == None:
        card_table = tables[0]
    else:
        card_table = Tables.objects.get(id_table=id_table)

    html_location = parse_html_path(TABLE_PATH,'list')
    response_dict = {
        'tables': tables,
        'card_table': card_table
    }
    return render(request, html_location, response_dict)

def get_table(request,id_table):
    try:
        table = get_object_or_404(Tables, id_table=id_table)
        html_location = parse_html_path(TABLE_PATH,'detail')
        response_dict = {
            'add': reverse('column_add',args=[crip(str(table.id_table))]),
            'look_all': reverse('columns_list',args=[crip(str(table.id_table))]),
            'exclude': reverse('column_add',args=[crip(str(table.id_table))]),
            'table': table
        }
        print(response_dict)
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('table_add')

def post(request):
    form = TablesForm(request.POST)
    print(form.errors)
    html_location = parse_html_path(TABLE_PATH,'add')

    if form.is_valid():
        table = form.save()
        return redirect('table_view', crip(str(table.id_table)))
    else:
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)

    # def put(self, request, id_company=None):
    #     company = get_object_or_404(Tables, id_company=id_company)
    #     form = TablesForm(request.POST, instance=company)
    #     html_location = self.parse_html_path('profile')
        
    #     response_dict = {
    #         'companies': form
    #     }
    #     if form.is_valid():
    #         form.save()
    #         return redirect('details_company', id=id_company)
    #     return render(request, html_location, response_dict)
    