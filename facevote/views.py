from django.shortcuts import render
from django.http import JsonResponse
from .main import find_match


# Create your views here.
def index(request):
    return render(request,'index.html')


def checkIdentity(request):
    if request.method == 'POST':
        print(request.FILES)
        photo = request.FILES['photo']
        elector_id = request.POST.get('electorId')
        print(elector_id)
        if find_match(elector_id,photo):
            print("CA marche")
            return JsonResponse({
                'message': 'True'
            })
    return JsonResponse({'message':'Indentity check failed'})