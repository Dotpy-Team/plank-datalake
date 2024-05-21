"""
plank_datalake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from business.routers import *
from process.routers import *
from process import views as p
from business import views as b


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', b.home_page , name='home_page'),

    # CUSTOMER:
    path('customer/', b.new_customer , name='new_customer'),
    path('customer-profile/', b.profile_customer, name='profile_customer'),
    path('admin-customer-profile/<str:customer_id>', b.admin_profile_customer, name='admin_profile_customer'),
    path('admin-customer-profiles/', b.admin_list_customers, name='admin_list_customers'),

    #CONTRACT
    path('contract/<str:customer_id>', b.new_contract , name='new_contract'),
    path('contract-details/<str:contract_id>', b.profile_contract , name='profile_contract'),
    path('admin-contract-list/', b.admin_list_contracts, name='admin_list_contracts'),
    path('contracts/<str:customer_id>', b.list_contracts, name='list_contracts'),

    #CONTRACT_ITEM
    path('contract-item/<str:contract_id>', b.new_contract_item, name='new_contract_item'),

    #CONTACT
    path('new-contact/<str:customer_id>', b.new_contact, name='new_contact'),
    path('profile-contact/<str:contact_id>', b.profile_contact, name='profile_contact'),
    path('list-contacts/', b.list_contacts_by_id, name='list_contacts_by_id'),
    path('admin-list-contacts/', b.list_contacts, name='list_contacts'),

    #USER:
    path('signup/<str:customer_id>', b.new_user , name='new_user'),
    path('login/', b.user_login, name='user_login'),
    path('logout/', b.user_logout, name='user_logout'),

    path('user-profile/', b.user_profile, name='user_profile'),
    path('user-profile/<str:email>', b.admin_user_profile, name='admin_user_profile'),
    path('users/<str:customer_id>', b.users_list_by_id_customer, name='users_list_by_id_customer'),
    path('all-users/', b.all_users, name='all_users'),    

    #TASK:
    path('task/<str:customer_id>', b.new_task_by_id_customer , name='new_task'),
    path('task-details/<str:task_id>', b.profile_task, name='profile_task'),

    #SERVICE:
    path('service/', b.new_service , name='new_service'),

    #SYSTEM:
    path('chose-system/', p.route, name='route'),
    path('system/', p.new_system , name='new_system'),
    path('sheets-system/', p.new_sheets_system, name='new_sheets_system'),
    path('postgre-system/', p.new_postgre_system, name='new_postgre_system'),
    path('mysql-system/', p.new_mysql_system, name='new_mysql_system'),
    path('sqlite-system/', p.new_sqlite_system, name='new_sqlite_system'),
    path('admin-system/<str:customer_id>', p.new_system , name='new_system'),

    path('systems/', p.list_system, name='list_system'),
    path('system-details/<str:system_id>', p.profile_system, name='profile_system'),

    path('admin-list-system/<str:customer_id>', p.admin_list_system, name='list_system'),

    #DATASET:
    path('dataset/<str:system_id>', p.new_dataset , name='new_dataset'),
    path('dataset-details/<str:dataset_id>', p.profile_dataset, name='profile_dataset'),
    path('all-dataset/', p.all_dataset, name='profile_dataset'),

    #RACI:
    path('raci/', p.new_raci , name='new_raci'),
    path('raci-details/<str:activity_id>', p.profile_raci , name='profile_raci'),
    path('raci-list/', p.list_contracts , name='list_contracts'),

    #RACI-RELATED:
    path('raci-related/<str:activity_id>', p.new_related , name='new_related'),

    #TABLES:
    path('add-table/<str:dataset_id>', p.new_table_by_id,name='new_table_by_id'),
    path('detail-table/<str:table_id>',p.get_table,name='table_view'),
    path('search-tables/',p.get_tables,name='view_tables'),
    path('search-tables/<str:table_id>',p.get_tables,name='view_tables_id'),

    #COLUMNS:
    path('add-column/<str:table_id>', p.new_column ,name='new_column'),

    #JOBS: adm
    path('add-execution/<str:table_id>', p.new_execution ,name='new_execution'),
    path('detail-execution/<str:job_id>', p.detail_execution ,name='detail_execution'),
    path('list-execution/<str:table_id>', p.list_execution, name="list_execution"),
    path('all-execution/', p.all_execution, name="all-execution"),
    # path('view-column/<str:argument>',TablesView.as_view(),name='column_detail'),
    # path('view-columns/<str:argument>',TablesView.as_view(),name='columns_list')

    #DEPENDENCIES:
    path('add-dependencies/<str:table_id>', p.new_dependencies ,name='new_dependencies'),
    path('list-dependencies/', p.list_dependecies ,name='list_dependecies'),
    path('detail-dependencies/<str:dependency_id>', p.detail_dependencies ,name='detail_dependencies'),

    #PIPELINE:
    path('new-pipeline/', p.new_pipeline ,name='new_pipeline'),
    path('detail-pipeline/<str:pipeline_id>', p.detail_pipeline ,name='detail_pipeline'),
    path('list-pipeline/', p.list_pipeline,name='list_pipeline'),

    #STEP:
    path('new-step/<str:pipeline_id>', p.new_step ,name='new_step'),
    path('new-child-table/<str:step_id>', p.new_child_table ,name='new_child_table'),
    path('detail-step/<str:step_id>', p.detail_step ,name='detail_step'),
    path('list-step/', p.list_step,name='list_step'),

    #TRIGGERS:
    path('add-trigger/', p.add_trigger, name='add_trigger'),
    path('detail-trigger/<str:trigger_id>', p.detail_trigger, name='detail_trigger'),
    path('list-trigger/', p.list_trigger, name='list_trigger'),

    #TOKEN URLS: 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

    #REST API:
    path("api/", include([
        path("", include(job_router.urls)),
        path("", include(customer_router.urls))
    ])),

    #TABLE API:
    path('table-by-trigger/<str:trigger_id>', p.list_table_by_trigger, name='list_table_by_trigger'),
    path('get-table-columns/<str:table_id>', p.get_table_columns, name='get_table_columns'),

    #JOB EXECUTION API: 
    path('get-job/<str:table_id>', p.get_job, name="get_job_api"),
    path('post-job/<str:table_id>', p.post_job, name="post-job-api"), 
    
    #CUSTOMER API: 
    path('customer-post/', b.post_customer, name="post_customer"),
    path('api-list-customer/', b.list_customer_api, name="list_customer_api"),
    path('get-customer-cnpj/<str:str_cnpj>', b.get_customer_by_cnpj, name="customer_by_cnpj"),
]
