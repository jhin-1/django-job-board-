from django.urls import path, include
from .job import urls as job_urls

urlpatterns = [
    path('job/', include(job_urls)),

]