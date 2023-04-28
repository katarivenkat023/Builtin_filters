from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse('inserted data successfully')
    return render(request,'insert_topic.html')
    

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        TO=Topic.objects.get(topic_name=topic)
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('insert_webpage successfully')
        
    
    return render (request,'insert_webpage.html',d)

def insert_access(request):
    wo=AccessRecord.objects.all()
    d={'access':wo}
    if request.method=='POST':
        name=request.POST['name']
        auther=request.POST['auther']
        wo=Webpage.objects.get(name=name)
        wo.save()
        ao=AccessRecord.objects.get_or_create(name=wo,auther=auther)[0]
        ao.save()
        return HttpResponse('insert_successfully')
    
    return render(request,'insert_access.html',d)
    