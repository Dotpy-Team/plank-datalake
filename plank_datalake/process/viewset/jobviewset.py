from rest_framework import viewsets
from process.models import JobRun
from process.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = JobRun.objects.all()
    serializer_class = JobSerializer
