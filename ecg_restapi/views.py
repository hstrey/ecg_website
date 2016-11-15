from ecg_graph.models import ECGdata
from ecg_restapi.serializers import ECGdataSerializer
from rest_framework import generics

class ECGdataList(generics.ListCreateAPIView):
    queryset = ECGdata.objects.all()
    serializer_class = ECGdataSerializer


class ECGdataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ECGdata.objects.all()
    serializer_class = ECGdataSerializer
