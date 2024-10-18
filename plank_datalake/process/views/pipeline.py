from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Pipeline, RaciActivity, Step, Tables, JobRun, Log
from business.models import Customer   
from process.forms import PipelineForm, StepForm
import base64
import requests
import boto3

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

PIPELINE_PATH = 'process/Pipeline/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location

@login_required
def new_pipeline(request):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    form = PipelineForm(request.POST)
    html_location = parse_html_path(PIPELINE_PATH,'new_pipeline')
    
    if request.method == 'POST':
        if form.is_valid(): 
            pipeline = form.save(commit=False)
            pipeline.customer = customer_instance
            pipeline.save()
            return redirect('detail_pipeline', crip(str(pipeline.pipeline_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            error_dict = {
                'form': form, 
                'error_message':error_message,
                'errors': form.errors 
            }
            return render(request, html_location, error_dict)
    else:
        form = PipelineForm()

        form.fields['raci_activity'].queryset = RaciActivity.objects.filter(customer_id=customer_id)
        form.fields['raci_activity'].widget.attrs['class'] = 'form-select'
        form.fields['raci_activity'].label = 'Raci'

        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)

@login_required 
def detail_pipeline(request, pipeline_id):
    pipeline_id = uncrip(pipeline_id)
    pipeline = get_object_or_404(Pipeline, pipeline_id=pipeline_id)
    
    aws_access_key_id = pipeline.customer.str_aws_access_key_id
    aws_secret_acces_key = pipeline.customer.str_aws_secret_key
    aws_region_name = pipeline.customer.str_aws_region 

    s3 = boto3.client(
        's3',
        aws_access_key_id= aws_access_key_id,
        aws_secret_access_key=aws_secret_acces_key,
        region_name= aws_region_name
    )

    bucket_name = 'aws-athena-query-results-us-east-1-121253776145'
    object_key = '01c15cb1-f6d1-4dd4-8f2e-75268d153835.csv'

    csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_data = csv_obj['Body'].read().decode('utf-8')

    rows = csv_data.split('\n')

    if rows:
        aws_table_header = rows[0].split(',')

        aws_table_rows = []
        for row in rows[1:]:
            aws_table_rows.append(row.split(','))
    else:
        aws_table_header = []
        aws_table_rows = []

    html_location = parse_html_path(PIPELINE_PATH, 'detail_pipeline')

    steps = Step.objects.filter(pipeline_id=pipeline_id)

    headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': request.COOKIES.get('csrftoken'),
    }

    log_list = []

    for step in steps:
        step.new_child_table = reverse('new_child_table', args=[crip(str(step.step_id))])

        try:
            step.table = Tables.objects.get(step_id=step.step_id)
            step.table.job = JobRun.objects.filter(table=step.table).order_by('job_id').last()
            step.table.log = Log.objects.filter(job=step.table.job).order_by('log_id').last()
        except Tables.DoesNotExist:
            step.table = None

        step.save()


    response_dict = {
        'pipeline': pipeline,
        'new_step': reverse('new_step', args=[crip(str(pipeline.pipeline_id))]),
        'headers': aws_table_header,
        'rows': aws_table_rows,
        'steps':steps
    }

    return render(request, html_location, response_dict)

@login_required
def list_pipeline(request):
    customer_id = request.user.customer.customer_id 
    customer = get_object_or_404(Customer, customer_id=customer_id)

    pipelines = Pipeline.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(PIPELINE_PATH, 'list_pipeline')

    # Configuração da paginação
    paginator = Paginator(pipelines, 6)  # 10 sistemas por página
    page = request.GET.get('page')

    try:
        pipelines = paginator.page(page)
    except PageNotAnInteger:
        pipelines = paginator.page(1)
    except EmptyPage:
        pipelines = paginator.page(paginator.num_pages)

    for pipeline in pipelines:
        pipeline.detail_url = reverse(
            'detail_pipeline',
            args=[crip(str(pipeline.pipeline_id))]
        )

        pipeline.save()

    response_dict = {
        'pipelines': pipelines
    }

    return render(request, html_location, response_dict)
