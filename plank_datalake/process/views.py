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

class TablesView(View):
    def __init__(self):
        self.template_path = 'process/Tables/'

    def parse_html_path(self,page):
        html_location = self.template_path + f'{page}.html'
        return html_location

    def render_add(self, request):
        form = TablesForm()
        html_location = self.parse_html_path('add')
        dict_form = {
            'form': form
        }
        return render(request, html_location, dict_form)
    
    def get_tables(self, request):
        print(request.user)
        tables = Tables.objects.all()
        for table in tables:
            table.detail_url = reverse(
                'table_view', 
                args=[crip(str(table.id_table))]
            )
            table.save()
        html_location = self.parse_html_path('list')
        response_dict = {'tables': tables}
        return render(request, html_location, response_dict)
    
    def get_table(self,request,id_table):
        try:
            table = get_object_or_404(Tables, id_table=id_table)
            html_location = self.parse_html_path('detail')
            response_dict = {'table': table}
            return render(request, html_location, response_dict)
        except Http404:
            return redirect('table_add')
    
    def get(self, request, argument=None):
        if request.path == '/add-table/':
            return self.render_add(request)
        elif argument is not None:
            id_tabela = uncrip(argument)
            return self.get_table(request,id_tabela)
        elif argument is None:
            return self.get_tables(request)


    def post(self, request):
        form = TablesForm(request.POST)
        print(form.errors)
        html_location = self.parse_html_path('add')

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
    