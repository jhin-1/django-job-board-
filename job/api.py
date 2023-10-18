# views

# from .models import Job
# # from .serializers import JobSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import generics


# @api_view(['Get'])
# def job_list_api(request):
#     all_jobs = Job.objects.all()
#     data = JobSerializer(all_jobs, many=True).data
#     return Response({'data': data})
#
#
# @api_view(['Get'])
# def job_details_api(request, id):
#     job_details = Job.objects.get(id=id)
#     data = JobSerializer(job_details).data
#     return Response({'data': data})


# class JobListApi(generics.ListAPIView):
#     model = Job
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer
#
#
# class JobDetails(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = JobSerializer
#     queryset = Job.objects.all()
#     lookup_field = 'id'
