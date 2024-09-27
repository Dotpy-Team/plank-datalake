from rest_framework import serializers
from business.models import Customer 


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            "customer_id",
            "str_customer_type",
            "str_name",
            "str_cnpj",
            "str_address",
            "str_telefone",
            "str_email",
            "str_site",
            "str_linkedin_profile",
            "str_contact",
            "str_setor",
            "str_size",
            "dth_create",
            "str_finance_complement",
            "str_documents",
            "str_comments",
            'str_aws_account_id',
            'str_aws_access_key_id',
            'str_aws_secret_key',
            'str_aws_region'
        ]