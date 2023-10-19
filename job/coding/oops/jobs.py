from ...models import Job
from rest_framework import status





class JobsOop:
    @staticmethod
    def all(request):
        re_data = None
        re_message = ""
        list_items = []
        get_all_items = Job.objects.all()
        for job in get_all_items:
            send = {
                "id": job.id,
                "title": job.title,
            }
            list_items.append(send)
        re_status = status.HTTP_200_OK
        re_message = "pes"
        re_data = {
            "list_items": list_items,
        }
        return [re_status, re_message, re_data]
    @staticmethod
    def details(request):
        re_data = None
        re_message = ""
        try:
            get_job = Job.objects.get(id=request.GET.get('job_id')) 
        except:
            get_job = None
        if get_job:
            re_status = status.HTTP_200_OK
            re_message = "pes"
            re_data = {
                "id": get_job.id,
                "description": get_job.description,
                "job_type": get_job.job_type,
            }
        else:
            re_status = status.HTTP_404_NOT_FOUND
            re_message = "not found 404"
        return [re_status, re_message, re_data]

