from rest_framework import serializers
from process.models import JobRun, Log

class JobRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRun
        fields = [
            "job_id",
            "customer",
            "table",
            "dth_start_at",
            "dth_ended_at",
            "str_status",
            "str_event_bucket_trigger",
            "str_event_key_trigger"
        ]

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = [
            'log_id',
            'job',
            'dth_event_at',
            'str_type',
            'str_desc'
        ]