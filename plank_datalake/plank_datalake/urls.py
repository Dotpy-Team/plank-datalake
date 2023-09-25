"""plank_datalake URL Configuration

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
# from business.views import CustomerView
from business import views as b


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', b.home_page , name='new_user'),
    #USER: adm
    path('signup/<str:id_customer>', b.new_user , name='new_user'),
    path('login/', b.user_login, name='user_login'),
    path('user-profile/<str:email>', b.user_profile, name='user_profile'),
    path('users/<str:id_customer>', b.users_list_by_id_customer, name='users_list_by_id_customer'),
    path('all-users/', b.users_list_by_id_customer, name='all_users'),
    # #CUSTOMER: adm

    path('customer/', b.new_customer , name='new_customer'),
    path('customer-profile/<str:id_customer>', b.customer_profile, name='profile_customer'),
    path('customer-profiles/', b.customers_list, name='list_customers'),



    # #TABLE adm
    path('add-table/', p.new_table,name='table_add'),
    path('detail-table/<str:argument>',p.get_table,name='table_view'),
    path('search-tables/<str:argument>',p.get_tables,name='table_view'),

    # #COLUMNS adm
    # path('add-column/<str:argument>', TablesView.as_view(),name='column_add'),
    # path('view-column/<str:argument>',TablesView.as_view(),name='column_detail'),
    # path('view-columns/<str:argument>',TablesView.as_view(),name='columns_list')

]
