from rest_framework import serializers
from process.models import JobRun 


class JobSerializer(serializers.ModelSerializer):

    class Meta: 
        model = JobRun
        fields = [
            'dth_last_updated',
            'dth_start_at',
            'str_status',
            'int_total_size',
            'int_total_rows'
        ]