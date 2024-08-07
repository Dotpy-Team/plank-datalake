from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from django.views import View
from business.models import Customer
from process.models import RaciActivity, RaciRelated
from process.forms import RaciActivityForm, RaciRelatedForm
from process.forms import raci
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

RACI_PATH = 'process/Raci/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location

@login_required
def new_raci(request):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        form = RaciActivityForm(request.POST)
        html_location = parse_html_path(RACI_PATH,'new_activity')

        form.fields['responsible'].queryset = customer_instance.customuser_set.all()
        form.fields['responsible'].widget.attrs['class'] = 'form-select'
        form.fields['responsible'].label = 'Responsavel'

        form.fields['accountable'].queryset = customer_instance.customuser_set.all()
        form.fields['accountable'].widget.attrs['class'] = 'form-select'
        form.fields['accountable'].label = 'Aprovador'

        if form.is_valid():
            raci = form.save(commit=False)
            raci.customer = customer_instance
            raci.str_status = "A"
            raci.save()
            return redirect('profile_raci', crip(str(raci.activity_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:

        form = RaciActivityForm()
        form.fields['responsible'].queryset = customer_instance.customuser_set.all()
        form.fields['responsible'].widget.attrs['class'] = 'form-select'
        form.fields['responsible'].label = 'Responsavel'

        form.fields['accountable'].queryset = customer_instance.customuser_set.all()
        form.fields['accountable'].widget.attrs['class'] = 'form-select'
        form.fields['accountable'].label = 'Aprovador'

        html_location = parse_html_path(RACI_PATH,'new_activity')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

@login_required
def new_related(request,activity_id):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home') 

    try:
        activity_id = uncrip(activity_id)
        activity_instance = RaciActivity.objects.get(activity_id=activity_id)
    except RaciActivity.DoesNotExist:
        return redirect('home') 


    if request.method == 'POST':

        form = RaciRelatedForm(request.POST)
        html_location = parse_html_path(RACI_PATH,'new_related')

        form.fields['person'].queryset = customer_instance.customuser_set.all()
        form.fields['person'].widget.attrs['class'] = 'form-select'
        form.fields['person'].label = 'Relacionado'

        if form.is_valid():
            related = form.save(commit=False)
            related.customer = customer_instance
            related.activity = activity_instance
            related.save()
            return redirect('profile_raci', crip(str(related.activity_id)))
        
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:

        form = RaciRelatedForm()
        
        form.fields['person'].queryset = customer_instance.customuser_set.all()
        form.fields['person'].widget.attrs['class'] = 'form-select'
        form.fields['person'].label = 'Relacionado'

        html_location = parse_html_path(RACI_PATH,'new_related')
        response_dict = {
            'form':form
        }
        return render(request, html_location, response_dict)

@login_required
def profile_raci(request,activity_id):
    # try:
    activity_id = uncrip(activity_id)
    activity = get_object_or_404(RaciActivity, activity_id=activity_id)
    html_location = parse_html_path(RACI_PATH,'profile_raci')

    related_type = request.GET.get('related_type')

    if related_type == 'informado':
        related = RaciRelated.objects.filter(activity_id=activity_id, str_type='INF')
    elif related_type == 'consultado':
        related = RaciRelated.objects.filter(activity_id=activity_id, str_type='CON')
    elif related_type == 'todos':
        related = RaciRelated.objects.filter(activity_id=activity_id)
    else:
        related = RaciRelated.objects.filter(activity_id=activity_id)

    customUser = Customer.objects.get(customer_id=activity.customer_id).customuser_set.all()

    paginator = Paginator(related, 6)
    page = request.GET.get('page')

    try:
        related_page = paginator.page(page)
    except PageNotAnInteger:
        related_page = paginator.page(1)
    except EmptyPage:
        related_page = paginator.page(paginator.num_pages)

    response_dict = {
        'activity': activity,
        'new_related' : reverse(
            'new_related',
            args=[crip(str(activity.activity_id))]
        ),
        'related': related_page,
        'related_type':related_type
    }
    return render(request, html_location, response_dict)

@login_required
def list_activities(request):
    customer_id = request.user.customer.customer_id
    customer = get_object_or_404(Customer, customer_id=customer_id)

    search = request.GET.get('search')
    raci = RaciActivity.objects.filter(customer_id=customer_id)

    if search:
        raci = raci.filter(str_title__icontains=search)

    raci = raci.order_by('activity_id')
    html_location = parse_html_path(RACI_PATH,'list_activity')

    for activity in raci:
        activity.detail_url = reverse(
            'profile_raci',
            args=[crip(str(activity.activity_id))]
        )
        activity.save()
    
    paginator = Paginator(raci, 6)  # Define 10 itens por página
    page = request.GET.get('page')
    
    try:
        raci_page = paginator.page(page)
    except PageNotAnInteger:
        raci_page = paginator.page(1)
    except EmptyPage:
        raci_page = paginator.page(paginator.num_pages)

    response_dict = {
        'raci': raci_page,
        'search': search
    }
    
    return render(request, html_location, response_dict)
