from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("منصة التوجيه الطلابي جاهزة للنشر")

urlpatterns=[
path('',home),
]
