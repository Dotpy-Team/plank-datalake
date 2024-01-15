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
from django.urls import path
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
    path('contracts/', b.list_contracts, name='list_contracts'),

    #CONTRACT_ITEM
    path('contract-item/<str:contract_id>', b.new_contract_item, name='new_contract_item'),

    #CONTACT
    path('new-contact/<str:customer_id>', b.new_contact, name='new_contact'),
    path('profile-contact/<str:contact_id>', b.profile_contact, name='profile_contact'),
    path('list-contacts/<str:customer_id>', b.list_contacts, name='list_contacts'),
    path('list-contacts/', b.list_contacts, name='list_contacts'),

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
    path('system/', b.new_system , name='new_system'),
    path('admin-system/<str:customer_id>', b.new_system , name='new_system'),

    path('systems/', b.list_system, name='profile_system'),
    path('system-details/<str:system_id>', b.profile_system, name='profile_system'),

    path('admin-list-system/<str:customer_id>', b.admin_list_system, name='list_system'),

    #DATASET:
    path('dataset/<str:system_id>', b.new_dataset , name='new_dataset'),
    path('dataset-details/<str:dataset_id>', b.profile_dataset, name='profile_dataset'),
    path('all-dataset/', b.all_dataset, name='profile_dataset'),

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
    # path('view-column/<str:argument>',TablesView.as_view(),name='column_detail'),
    # path('view-columns/<str:argument>',TablesView.as_view(),name='columns_list')

]
