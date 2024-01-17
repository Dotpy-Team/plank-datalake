from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Pipeline
from business.models import Customer   
from process.forms import PipelineForm
import base64

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
    else:
        form = PipelineForm()
        response_dict = {
            'form': form
        }
        return render(request, html_location, response_dict)
    
def detail_pipeline(request, pipeline_id):
    pipeline_id = uncrip(pipeline_id)

    pipeline = get_object_or_404(Pipeline, pipeline_id=pipeline_id)
    html_location = parse_html_path(PIPELINE_PATH, 'detail_pipeline')
    response_dict = {
        'pipeline': pipeline
    }

    return render(request, html_location, response_dict)

def list_pipeline(request):
    customer_id = request.user.customer.customer_id 
    customer = get_object_or_404(Customer, customer_id=customer_id)

    pipelines = Pipeline.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(PIPELINE_PATH, 'list_pipeline')

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
