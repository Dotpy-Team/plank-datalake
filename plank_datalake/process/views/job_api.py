from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from business.models import Customer
from process.models import Tables, JobRun, LogRequest
from process.serializers import JobRunSerializer, jobrunserializer

import json


@api_view(["POST"])
def post_job(request, table_id):
    
    response = request.data
    print(dir(response))

    try:
        table = Tables.objects.get(table_id=table_id)
        response["customer"] = table.customer_id
        response["table"] = table.table_id
    except Tables.DoesNotExist:
        error = {"table_id":[ 'Table no found.']}
        log_request = LogRequest.objects.create(
            customer_id=1,
            str_url=request.path,
            str_method="POST",
            str_request_body=response,
            str_response_status=412,
            str_response_body= error
        )
        log_request.save() 
        return Response(error, status=412)
    
    job_serializer = JobRunSerializer(data=response)

    if job_serializer.is_valid():
        job_serializer.save()
        return Response(job_serializer.data)
    else:
        return Response(job_serializer.errors, status=412)


@api_view(["GET"])
def get_job(request, table_id):
    job = JobRun.objects.filter(table_id=table_id)
    serializer = JobRunSerializer(job, many=True)
    return Response(serializer.data)
