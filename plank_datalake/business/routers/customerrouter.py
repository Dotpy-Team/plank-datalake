from rest_framework import routers
from business.viewset import CustomerViewSet


customer_router = routers.DefaultRouter()
customer_router.register(r'customers', CustomerViewSet, basename="customer_api")
