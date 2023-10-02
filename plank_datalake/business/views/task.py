from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import Task
from business.forms import TaskForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

def parse_html_path(template_path,page):
    html_location = template_path + f'{page}.html'
    return html_location



#######################################
"""
TASK NEW_TASK
TASK PROFILE_TASK

"""
#######################################

TASK_PATH = 'business/Task/'

def new_task_by_id_customer(request,id_customer):
    id_customer = uncrip(id_customer)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        html_location = parse_html_path(TASK_PATH,'new_task')

        if form.is_valid():
            task = form.save()
            return redirect('profile_task', crip(str(task.id_task)))
        else:
            print(form.errors)
            response_dict = {'form': form}
            return render(request, html_location, response_dict)
    else:
        form = TaskForm(
            initial={
                'id_customer': id_customer,
                'id_table':0})
        html_location = parse_html_path(TASK_PATH,'new_task')
        dict_form = {
            'form': form
        }
    return render(request, html_location, dict_form)

def profile_task(request,id_task):
    id_task = uncrip(id_task)
    # try:
    task = get_object_or_404(Task, id_task=id_task)
    html_location = parse_html_path(TASK_PATH,'profile_task')
    response_dict = {
        'task': task
    }
    return render(request, html_location, response_dict)
    # except Http404:
    #     return redirect('signup_company')
