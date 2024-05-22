from rest_framework import serializers
from process.models import JobRun


class JobRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRun
        fields = [
            "job_id",
            "customer",
            "table",
            "dth_last_updated",
            "dth_start_at",
            "str_status",
            "int_total_size",
            "int_total_rows",
            "str_event_bucket_trigger",
            "str_event_key_trigger"
        ]