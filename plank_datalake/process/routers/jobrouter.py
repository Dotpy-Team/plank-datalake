from rest_framework import routers
from process.viewset import JobViewSet 


job_router = routers.DefaultRouter()
job_router.register(r'jobs', JobViewSet, basename='job')