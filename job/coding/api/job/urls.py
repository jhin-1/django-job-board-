from django.urls import path, include
from .code import *

urlpatterns = [
    path('all', all_api),
    path('details', details_api),
    path('create', create_api),

]