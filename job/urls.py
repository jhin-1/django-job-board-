from django.urls import path, include
from . import views
from . import api
from .coding import urls as coding_urls

app_name = 'job'
urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_details, name='job_details'),
    # path('api/jobs', api.job_list_api, name='job_list_api'),
    # path('api/jobs/<int:id>', api.job_details_api, name='job_details_api'),
    path('dash/', include(coding_urls)),

    # class based views
    # path('api/v2/jobs', api.JobListApi.as_view(), name='job_list_api'),
    # path('api/jobs/v2/<int:id>', api.JobDetails.as_view(), name='job_details_api'),

]
