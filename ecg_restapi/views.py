from ecg_graph.models import ECGdata
from ecg_restapi.serializers import ECGdataSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class EcgDataList(generics.ListCreateAPIView):
    serializer_class = ECGdataSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ECGdata.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, created_data=timezone.now())


class EcgDataDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ECGdataSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ECGdata.objects.filter(owner=user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
