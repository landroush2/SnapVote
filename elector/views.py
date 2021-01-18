from django.shortcuts import render

# Create your views here.

from api.serializers import FileSerializer


def video(request):
    return render(request,'index.html')

