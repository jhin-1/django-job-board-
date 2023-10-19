from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...oops.jobs import *
from ...oops import *
# http://127.0.0.1:8000/dash/api/job/all
# http://127.0.0.1:8000/dash/api/job/details

@api_view(["GET"])
def all_api(request):
    call = JobsOop.all(request)
    re_status, re_message, re_data = call[0], call[1], call[2]
    re_send = {
        "message": re_message,
        "data": re_data
    }
    return Response(re_send, re_status)


@api_view(["GET"])
def details_api(request):
    call = JobsOop.details(request)
    re_status, re_message, re_data = call[0], call[1], call[2]
    re_send = {
        "message": re_message,
        "data": re_data
    }
    return Response(re_send, re_status)

