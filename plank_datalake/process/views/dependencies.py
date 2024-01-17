from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.views import View
from process.models import Tables, Dependencies
from business.models import Customer   
from process.forms import DependenciesForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

DEPENDENCIES_PATH = 'process/Dependecies/'

def parse_html_path(path,page):
    html_location = path + f'{page}.html'
    return html_location


def new_dependencies(request):
    try:
        customer_id = request.user.customer.customer_id
        customer_instance = Customer.objects.get(customer_id=customer_id)
    except Customer.DoesNotExist:
        return redirect('home')

    if request.method =='POST': 
        form = DependenciesForm(request.POST)
        html_location = parse_html_path(DEPENDENCIES_PATH,'new_dependencies')

        if form.is_valid(): 
            dependency = form.save(commit=False)  
            dependency.customer = customer_instance
            dependency.save()
            return redirect('detail_dependencies', crip(str(dependency.dependency_id)))
        else:
            error_message = 'Credenciais inválidas. Por favor, tente novamente.'
            response_dict = {
                'form': form,
                'error_message':error_message,
                'error_forms':form.errors
            }
            return render(request, html_location, response_dict)
    else:
        form = DependenciesForm()
        form.fields['table_node'].queryset = customer_instance.tables_set.all()
        form.fields['table_node'].widget.attrs['class'] = 'form-select'
        form.fields['table_node'].label = 'Tabela'
        
        form.fields['table_edge'].queryset = customer_instance.tables_set.all()
        form.fields['table_edge'].widget.attrs['class'] = 'form-select'
        form.fields['table_edge'].label = 'Tabela'
        
        html_location = parse_html_path(DEPENDENCIES_PATH,'new_dependencies')
        response_dict = {
            'form': form,
        }
        return render(request, html_location, response_dict)
    
def list_dependecies(request):
    customer_id = request.user.customer.customer_id
    customer = get_object_or_404(Customer, customer_id=customer_id)

    dependencies = Dependencies.objects.filter(customer_id=customer_id)
    html_location = parse_html_path(DEPENDENCIES_PATH,'list')
    
    for dependency in dependencies:
        dependency.detail_url = reverse(
            'detail_dependencies', 
            args=[crip(str(dependency.dependency_id))]
        )

        dependency.save()
        

    response_dict = {
        'dependency': dependencies    
    }
    return render(request, html_location, response_dict)

def detail_dependencies(request,dependency_id):
    dependency_id = uncrip(dependency_id)
    dependency = get_object_or_404(Dependencies, dependency_id=dependency_id)
    html_location = parse_html_path(DEPENDENCIES_PATH,'detail')
    response_dict = {
        'dependency': dependency
    }
    return render(request, html_location, response_dict)