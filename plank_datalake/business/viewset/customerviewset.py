from rest_framework import viewsets
from business.models import Customer
from business.serializers import CustomerSerializer 


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
