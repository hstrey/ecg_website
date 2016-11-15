from ecg_graph.models import ECGdata
from ecg_restapi.serializers import ECGdataSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class ECGdataList(generics.ListCreateAPIView):
    queryset = ECGdata.objects.all()
    serializer_class = ECGdataSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ECGdataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ECGdata.objects.all()
    serializer_class = ECGdataSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
