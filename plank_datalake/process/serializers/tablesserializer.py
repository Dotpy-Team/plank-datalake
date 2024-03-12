from rest_framework import serializers 
from process.models import Tables 


class TablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tables 
        fields = [
            'customer',
            'dataset',
            'step', 
            'layer', 
            'str_frequency', 
            'str_type_of',
            'str_mode',
            'str_type', 
            'str_name', 
            'str_desc', 
            'str_desc_ia', 
            'raci_activity',
            'dth_start_at',
            'dth_last_updated', 
            'int_size', 
            'int_number_of_rows', 
            'float_perc_growth',
            'trigger' 
        ]