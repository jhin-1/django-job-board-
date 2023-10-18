from django.urls import path, include
from .code import *

urlpatterns = [
    path('all', all_api),

]