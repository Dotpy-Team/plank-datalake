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
from process.views import TablesView
from business.views import CustomUserView, CustomerView

urlpatterns = [
    path('admin/', admin.site.urls),
    #home page
    path('',CustomUserView.as_view(), name='home'),
    #CUSTOMER: adm
    path('customer/', CustomerView.as_view(), name='add'),
    path('customer-profile/<str:argument>', CustomerView.as_view(), name='profile_customer'),
    path('customer-profiles/', CustomerView.as_view(), name='list_customers'),
    #USER: adm
    path('signup/', CustomUserView.as_view(), name='signup'),
    path('login/', CustomUserView.as_view(), name='login'),
    # path('login/', TablesView.as_view(), name='login'),
    # path('logout/', TablesView.as_view(), name='logout'),
    path('profile/<str:argument>', CustomUserView.as_view(), name='user_profile'),
    #TABLE adm
    path('add-table/', TablesView.as_view(),name='table_add'),
    path('view-table/<str:argument>',TablesView.as_view(),name='table_view'),
    path('view-tables/',TablesView.as_view(),name='table_view')
]
