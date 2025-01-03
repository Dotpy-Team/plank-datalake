from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from business.models import Customer
from business.serializers import CustomerSerializer
from process.models import Step, JobRun, Log, Tables
from process.serializers import StepSerializer
import json
from datetime import datetime
import boto3
import botocore


@api_view(["POST"])
def execute_query(request, step_id):
    api_response = request.data

    serializer = StepSerializer

    try:
        step = Step.objects.get(step_id=step_id)
        table = Tables.objects.get(step=step_id)
        customer_id = step.customer.customer_id
        query = step.str_query
    except Step.DoesNotExist:
        print('Query não encontrada.')

    print(table)

    try:
        customer= Customer.objects.get(customer_id=customer_id)
        aws_account_id = customer.str_aws_account_id
        aws_platform_acess_key_id = customer.str_aws_access_key_id
        aws_platform_secret_acess_key = customer.str_aws_secret_key
        aws_platform_region = customer.str_aws_region
    except Customer.DoesNotExist:
        print('Cliente não encontrado.')

    athena = boto3.client(
        'athena', 
        aws_access_key_id= aws_platform_acess_key_id,
        aws_secret_access_key=aws_platform_secret_acess_key,
        region_name=aws_platform_region
    )

    query_string = str(query)

    s3_output = f's3://aws-athena-query-results-{aws_platform_region}-{aws_account_id}/'

    query_execution_id = None
    dth_start_at = None

    try:
        query_execution = athena.start_query_execution(
            QueryString=query_string,
            ResultConfiguration={'OutputLocation': s3_output}
        )

        query_execution_id = query_execution['QueryExecutionId']
        print(query_execution_id)

        response = query_execution_id

        now = datetime.now()
        dth_start_at = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' -0300'
        
        job_run = JobRun(
            customer = customer,
            step = step,
            table = table,
            dth_start_at = dth_start_at,
            str_athena_execution_id = query_execution_id
        )

        job_run.save()
    except Exception as e:
        error_message= str(e)

        now = datetime.now()
        dth_event_at = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' -0300'
        
        job_run = JobRun(
            customer=customer,
            step=step,
            table = table,
            str_status= 'FAILED',
            dth_start_at = dth_event_at
        )
        
        job_run.save()

        log = Log(
            job = job_run,
            dth_event_at = dth_event_at,
            str_type = 'ERROR',
            str_desc = error_message
        )

        log.save()

        response = error_message

    return Response(response)

@api_view(['POST'])
def update_jobrun_athena(request, job_id):
    response = request.data

    try:
        job = JobRun.objects.get(job_id=job_id)
        customer_id = job.customer.customer_id
        query_execution_id = job.str_athena_execution_id
    except JobRun.DoesNotExist:
        pass

    try:
        customer = Customer.objects.get(customer_id=customer_id)
        aws_platform_acess_key_id = customer.str_aws_access_key_id
        aws_platform_secret_acess_key = customer.str_aws_secret_key
        aws_platform_region = customer.str_aws_region
    except Customer.DoesNotExist:
        pass

    athena = boto3.client(
        'athena',
        aws_access_key_id= aws_platform_acess_key_id,
        aws_secret_access_key=aws_platform_secret_acess_key,
        region_name=aws_platform_region
    )

    response = athena.get_query_execution(
        QueryExecutionId = query_execution_id
    )

    query_execution = response['QueryExecution']
    query_execution_status = query_execution['Status']
    query_execution_state = query_execution_status['State']

    now = datetime.now()
    dth_ended_at = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' -0300'

    job.dth_ended_at = dth_ended_at
    job.str_status = query_execution_state

    job.save()

    return Response(query_execution_state)
