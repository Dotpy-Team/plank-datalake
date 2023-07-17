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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TablesView.as_view(), name='login'),
    path('logout/', TablesView.as_view(), name='logout'),
    path('add-table/', TablesView.as_view(),name='table_add'),
    path('view-table/<str:argument>',TablesView.as_view(),name='table_view'),
    path('view-tables/',TablesView.as_view(),name='table_view')
]
