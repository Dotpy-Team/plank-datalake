from rest_framework import routers
from process.viewset import JobExecViewSet


job_router = routers.DefaultRouter()
job_router.register(r'jobs', JobExecViewSet, basename="job_execution")