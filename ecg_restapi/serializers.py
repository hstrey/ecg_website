from rest_framework import serializers
from ecg_graph.models import ECGdata

class ECGdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECGdata
        fields = ('id', 'created_date', 'data_json', 'owner')
