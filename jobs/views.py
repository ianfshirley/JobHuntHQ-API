from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Job
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated


class JobList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer