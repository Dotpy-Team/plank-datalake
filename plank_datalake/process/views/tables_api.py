from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from process.models import Tables 
from process.serializers import TablesSerializer


class GetTableByTrigger(APIView):

    def get_table(self, request): 
        table = request.table 
        table = Tables.objects.get(trigger=table)
        serializer = TablesSerializer(table)
        return Response(serializer.data)        
