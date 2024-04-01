from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from business.models import Customer
from business.serializers import CustomerSerializer


@api_view(["POST"])
def post_customer(request):
    serializer = CustomerSerializer(data=request.data)
        
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["GET"])
def list_customer_api(request):

    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_customer_by_cnpj(request, str_cnpj):
    cnpj = str_cnpj
    
    customer = Customer.objects.filter(str_cnpj=cnpj)
    print(customer)
    customer_values = customer.values()

    return Response(customer_values)