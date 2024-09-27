from rest_framework import serializers
from process.models import Step

class StepSerializer(serializers.ModelSerializer):

    model=Step
    fields=[
        'step_id',
        'str_query'
    ]
