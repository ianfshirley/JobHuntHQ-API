from django.urls import path
from . import views
from .views import JobList, JobDetail

urlpatterns = [
    path("", JobList.as_view(), name="job_list"),
    path("<int:pk>/", JobDetail.as_view(), name="job_detail"),
]