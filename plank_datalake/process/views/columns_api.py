from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from process.models import Tables, Columns 
from process.serializers import TablesSerializer

@api_view(['GET'])
def get_table_columns(request, table_id):

    try:
        tables_id = Tables.objects.get(table_id=table_id)
    except Tables.DoesNotExist:
        return Response('Tables not found')
    
    tables = Tables.objects.filter(table_id=table_id).values('table_id', 'str_name', 'str_separador')

    for row in tables:
        id = row['table_id']
        name = row['str_name']
        sep = row['str_separador']

    columns = Columns.objects.filter(table_id=tables_id).values('id_column', 'str_source_name', 'str_datatype')

    response_dict = {
        "id": id,
        "nome": name,
        "sep": sep,
        "columns": columns
    }

    return Response(response_dict)