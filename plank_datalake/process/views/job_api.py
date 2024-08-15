from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from business.models import Customer
from process.models import Tables, JobRun, Log
from process.serializers import JobRunSerializer, LogSerializer
import json

@api_view(["POST"])
def post_job(request, table_id):
    response = request.data
    try:
        table = Tables.objects.get(table_id=table_id)
        response["customer"] = table.customer_id
        response["table"] = table.table_id
    except Tables.DoesNotExist:
        error = {"table_id":[ 'Table no found.']}
        return Response(error, status=412)
    
    job_serializer = JobRunSerializer(data=response)

    if job_serializer.is_valid():
        job_serializer.save()
        return Response(job_serializer.data)
    else:
        return Response(job_serializer.errors, status=412)

@api_view(["POST"])
def post_log(request, job_id):
    response = request.data

    try:
        job = JobRun.objects.get(job_id=job_id)
        response["job"] = job.job_id
    except JobRun.DoesNotExist:
        error = {"job":[ 'Job Doesnt found.']}
        return Response(error, status=412)

    log_serializer = LogSerializer(data=response)

    if log_serializer.is_valid():
        log_serializer.save()
        return Response(log_serializer.data)
    else:
        return Response(log_serializer.errors, status=412)


@api_view(["GET"])
def get_job(request, table_id):
    job = JobRun.objects.filter(table_id=table_id)
    serializer = JobRunSerializer(job, many=True)
    return Response(serializer.data)
