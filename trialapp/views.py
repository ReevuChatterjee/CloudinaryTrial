from django.shortcuts import render,HttpResponse
from .models import DB

def home(request):
    obj=None
    if request.method=='POST':
        name=request.POST.get('name')
        image=request.FILES.get('photo')
        if name and image:
            obj=DB.objects.create(name=name,image=image)
    return render(request,'home.html',{'uploaded_obj':obj})

# Create your views here.
