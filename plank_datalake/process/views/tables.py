from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.urls import reverse
from django.http import Http404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from process.models import Tables, Columns, Trigger, DataSet, System, JobRun
from business.models import Customer
from process.forms import TablesForm, TablesWithOutDatasetForm
from process.serializers import TablesSerializer
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

TABLE_PATH = 'process/tables/'

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
        form.fields['trigger'].queryset = Trigger.objects.filter(customer_id=customer_id)
        form.fields['trigger'].widget.attrs['class'] = 'form-select'
        form.fields['trigger'].label = 'Trigger'

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
        
        form.fields['trigger'].queryset = Trigger.objects.filter(customer_id=customer_id)
        form.fields['trigger'].widget.attrs['class'] = 'form-select'
        form.fields['trigger'].label = 'Trigger'

        html_location = parse_html_path(TABLE_PATH,'add')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

@login_required
def new_table_without_dataset(request):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    if request.method == 'POST':
        form = TablesWithOutDatasetForm(request.POST)


        form.fields['trigger'].queryset = Trigger.objects.filter(customer_id=customer_id)
        form.fields['trigger'].widget.attrs['class'] = 'form-select'
        form.fields['trigger'].label = 'Trigger'

        html_location = parse_html_path(TABLE_PATH,'new_table_without_dataset')
        
        if form.is_valid():
            table = form.save(commit=False)
            table.customer = customer_instance
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
        form = TablesWithOutDatasetForm()

        form.fields['dataset'].queryset = DataSet.objects.filter(system__customer_id=customer_id)
        form.fields['dataset'].widget.attrs['class'] = 'form-select'
        form.fields['dataset'].label = 'dataset'


        form.fields['trigger'].queryset = Trigger.objects.filter(customer_id=customer_id)
        form.fields['trigger'].widget.attrs['class'] = 'form-select'
        form.fields['trigger'].label = 'Trigger'

        html_location = parse_html_path(TABLE_PATH,'new_table_without_dataset')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

@login_required
def get_tables(request):
    customer_id = request.user.customer.customer_id
    tables = Tables.objects.filter(customer_id=customer_id).order_by('table_id')
    for table in tables:
        table.detail_url = reverse('table_view', args=[crip(str(table.table_id))])
        table.save()

    search = request.GET.get('search')

    if search:
        tables = tables.filter(
            Q(str_name__icontains=search) | Q(dataset__str_title__icontains=search) | Q(dataset__system__str_title__icontains=search)
        )
    
    paginator = Paginator(tables, 6)
    page = request.GET.get('page')

    try:
        tables = paginator.page(page)
    except PageNotAnInteger:
        tables = paginator.page(1)
    except EmptyPage:
        tables = paginator.page(paginator.num_pages)

    html_location = parse_html_path(TABLE_PATH,'list')
    response_dict = {
        'tables': tables,
        'search':search
    }
    return render(request, html_location, response_dict)

@login_required
def get_table(request,table_id):
    try:
        table_id = uncrip(table_id)
        table = Tables.objects.get(table_id=table_id)
        columns = Columns.objects.filter(table_id=table_id)
        html_location = parse_html_path(TABLE_PATH,'detail')

        executions = JobRun.objects.filter(table_id=table_id)

        executions = executions.order_by('-job_id')

        for execution in executions:
            execution.detail_url = reverse('detail_execution',args=[crip(str(execution.job_id))])

        paginator = Paginator(executions, 6)  # 10 datasets por página
        page = request.GET.get('page')
        
        try:
            executions = paginator.page(page)
        except PageNotAnInteger:
            executions = paginator.page(1)
        except EmptyPage:
            executions = paginator.page(paginator.num_pages)

        response_dict = {
            'add': reverse('new_column',args=[crip(str(table.table_id))]),
            'new_job': reverse('new_execution',args=[crip(str(table.table_id))]),
            'view_job': reverse('detail_execution', args=[crip(str(table.table_id))]),
            'list_job': reverse('list_execution', args=[crip(str(table.table_id))]),
            'new_dependencie': reverse('new_dependencies', args=[crip(str(table.table_id))]),
            'table': table,
            'columns': columns,
            'executions':executions
        }
        return render(request, html_location, response_dict)
    except Http404:
        return redirect('table_add')

