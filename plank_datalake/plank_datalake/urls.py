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
    path('customer-profile/<str:id_customer>', b.profile_customer_by_id, name='profile_customer_by_id'),
    path('customer-profiles/', b.list_customers, name='list_customers'),

    #CONTRACT
    path('contract/<str:id_customer>', b.new_customer , name='new_customer'),


    #USER:
    path('signup/<str:id_customer>', b.new_user , name='new_user'),
    path('login/', b.user_login, name='user_login'),
    path('logout/', b.user_logout, name='user_logout'),

    path('user-profile/<str:email>', b.user_profile, name='user_profile'),
    path('users/<str:id_customer>', b.users_list_by_id_customer, name='users_list_by_id_customer'),
    path('all-users/', b.all_users, name='all_users'),    

    #TASK
    path('task/<str:id_customer>', b.new_task_by_id_customer , name='new_task'),
    path('task-details/<str:id_task>', b.profile_task, name='profile_task'),

    #SYSTEM:
    path('system/<str:id_customer>', b.new_system , name='new_system'),
    path('system-details/<str:id_system>', b.profile_system, name='profile_system'),

    #DATASET:
    path('dataset/<str:id_system>', b.new_dataset , name='new_dataset'),
    path('dataset-details/<str:id_dataset>', b.profile_dataset, name='profile_dataset'),


    #TABLE
    path('add-table/', p.new_table,name='new_table'),
    path('add-table/<str:id_customer>', p.new_table_by_id,name='new_table_by_id'),
    path('detail-table/<str:id_table>',p.get_table,name='table_view'),
    path('search-tables/<str:id_customer>',p.get_tables,name='view_tables'),

    # #COLUMNS adm
    # path('add-column/<str:argument>', TablesView.as_view(),name='column_add'),
    # path('view-column/<str:argument>',TablesView.as_view(),name='column_detail'),
    # path('view-columns/<str:argument>',TablesView.as_view(),name='columns_list')

]
