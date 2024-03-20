from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from process.models import Tables, Trigger 
from process.serializers import TablesSerializer

@api_view(['GET'])
def list_table_by_trigger(request, trigger_id):

    try:
        trigger = Trigger.objects.get(trigger_id = trigger_id)
    except Trigger.DoesNotExist:
        return Response('Trigger does not exist')
    
    tables = Tables.objects.filter(trigger_id=trigger)
    table_values = tables.values()
    # table_list = TablesSerializer(table_values).data

    return Response(table_values)