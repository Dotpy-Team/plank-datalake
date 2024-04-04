from rest_framework import serializers
from process.models import LogRequest


class LogRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogRequest
        fields = [
            "request_id",
            "customer",
            "str_url",
            "str_method",
            "str_request_body",
            "str_response_status",
            "str_response_body"
        ]
