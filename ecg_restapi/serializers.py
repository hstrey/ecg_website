from rest_framework import serializers
from django.contrib.auth.models import User
from ecg_graph.models import ECGdata


class ECGdataSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = ECGdata
        fields = ('id', 'created_date', 'data_json', 'owner')


class UserSerializer(serializers.ModelSerializer):
    ecgdata = serializers.PrimaryKeyRelatedField(many=True, queryset=ECGdata.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'ecgdata')
