from rest_framework import viewsets
from process.models import JobRun 
from process.serializers import JobRunSerializer


class JobExecViewSet(viewsets.ModelViewSet):
    queryset = JobRun.objects.all()
    serializer_class = JobRunSerializer