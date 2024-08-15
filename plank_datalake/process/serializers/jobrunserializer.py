from rest_framework import serializers
from process.models import JobRun

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