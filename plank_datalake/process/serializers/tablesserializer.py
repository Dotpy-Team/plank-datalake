from rest_framework import serializers 
from process.models import Tables 


class TablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tables 
        fields = [
            "str_frequency",
            "str_type_of",
            "str_mode",
            "str_type",
            "str_name",
            "str_desc",
            "str_desc_ia",
            'raci_activity',
            'trigger'
        ]