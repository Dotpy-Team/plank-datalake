from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from business.models import Customer
from process.models import Tables, JobRun
from process.serializers import JobExecSerializer


@api_view(['GET', 'POST'])
def job_api(request, table_id):

    try:
        tables = Tables.objects.get(table_id=table_id)
    except Tables.DoesNotExist:
        return Response('Tables not exist')
    
    if request.method == "GET":
        job = JobRun.objects.filter(table_id = tables)
        serializer = JobExecSerializer(job, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = JobExecSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response('Deu errado')