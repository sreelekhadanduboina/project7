from django.urls import path
from app2.views import *
app2_name='anything1'
urlpatterns = [
    path("htmlfile1/",htmlfile1,name="htmlfile1"),
]
