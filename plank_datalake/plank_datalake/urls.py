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
    path('admin-customer-profile/<str:id_customer>', b.admin_profile_customer, name='admin_profile_customer'),
    path('admin-customer-profiles/', b.admin_list_customers, name='admin_list_customers'),

    #CONTRACT
    path('contract/<str:id_customer>', b.new_contract , name='new_contract'),
    path('contract-details/<str:id_contract>', b.profile_contract , name='profile_contract'),
    path('admin-contract-list/', b.admin_list_contracts, name='admin_list_contracts'),

    #CONTRACT_ITEM
    path('contract-item/<str:id_contract>', b.new_contract_item, name='new_contract_item'),


    #USER:
    path('signup/<str:id_customer>', b.new_user , name='new_user'),
    path('login/', b.user_login, name='user_login'),
    path('logout/', b.user_logout, name='user_logout'),

    path('user-profile/<str:email>', b.user_profile, name='user_profile'),
    path('users/<str:id_customer>', b.users_list_by_id_customer, name='users_list_by_id_customer'),
    path('all-users/', b.all_users, name='all_users'),    

    #TASK:
    path('task/<str:id_customer>', b.new_task_by_id_customer , name='new_task'),
    path('task-details/<str:id_task>', b.profile_task, name='profile_task'),

    #SERVICE:
    path('service/', b.new_service , name='new_service'),

    #SYSTEM:
    path('system/<str:id_customer>', b.new_system , name='new_system'),
    path('system-details/<str:id_system>', b.profile_system, name='profile_system'),
    path('all-system/', b.list_system, name='list_system'),

    #DATASET:
    path('dataset/<str:id_system>', b.new_dataset , name='new_dataset'),
    path('dataset-details/<str:id_dataset>', b.profile_dataset, name='profile_dataset'),
    path('datasets/', b.all_dataset, name='profile_dataset'),

    #TABLES:
    path('add-table/<str:id_dataset>', p.new_table_by_id,name='new_table_by_id'),
    path('detail-table/<str:id_table>',p.get_table,name='table_view'),
    path('search-tables/',p.get_tables,name='view_tables'),

    # #COLUMNS adm
    # path('add-column/<str:argument>', TablesView.as_view(),name='column_add'),
    # path('view-column/<str:argument>',TablesView.as_view(),name='column_detail'),
    # path('view-columns/<str:argument>',TablesView.as_view(),name='columns_list')

]
