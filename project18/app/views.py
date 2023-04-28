from django.shortcuts import render

# Create your views here.
import datetime
def filter(request):
    d1=datetime.datetime.now
    d={'data':'hai this is venkat','date':d1}
    
    return render(request,'filter.html',d)