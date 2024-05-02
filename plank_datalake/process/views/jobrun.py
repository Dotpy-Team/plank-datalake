from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Tables, RaciActivity, JobRun
from business.models import Customer
from process.forms import ColumnsForm, JobRunForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

JOB_PATH = 'process/JobRuns/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location

@login_required
def new_execution(request, table_id):
    try:
        table_id = uncrip(table_id)
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
        table_instance = Tables.objects.get(table_id=table_id)
    except Customer.DoesNotExist:
        return redirect('home')
    
    if request.method == 'POST':
        form = JobRunForm(request.POST)
        html_location = parse_html_path(JOB_PATH,'add')
        if form.is_valid():
            job = form.save(commit=False)
            job.customer = customer_instance
            job.table = table_instance
            job.save()
            return redirect('detail_execution', crip(str(job.job_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:
        form = JobRunForm()

        html_location = parse_html_path(JOB_PATH,'add')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

@login_required
def detail_execution(request,job_id):
    job_id = uncrip(job_id)

    job = get_object_or_404(JobRun, job_id=job_id)
    html_location = parse_html_path(JOB_PATH, 'detail')
    response_dict = {
        'job': job
    }

    return render(request, html_location, response_dict)
    
@login_required
def list_execution(request, table_id):
    table_id = uncrip(table_id)

    jobs = JobRun.objects.filter(table_id=table_id)
    html_location = parse_html_path(JOB_PATH, 'list')

    for job in jobs:
        job.detail_url = reverse(
            'detail_execution',
            args=[crip(str(job.job_id))]
        )

        job.save()

    response_dict = {
        "jobs": jobs
        # "new-execution": reverse('add_execution', args=[crip(str())])
    }

    return render(request, html_location, response_dict)

@login_required
def all_execution(request):
    customer_id = request.user.customer.customer_id 

    jobs = JobRun.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(JOB_PATH, 'list')

    for job in jobs:
        job.detail_url =  reverse(
            'detail_execution',
            args=[crip(str(job.job_id))]
        )

        job.save()

    response_dict = {
        "jobs": jobs
    }

    return render(request, html_location, response_dict)
