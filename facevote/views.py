from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

@csrf_exempt
def checkIdentity(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        uploaded_file_url = fs.url(filename)
        return JsonResponse({
            'uploaded_file_url' : uploaded_file_url
        })
    return JsonResponse({'error':'Indentity check failed'})