from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':1000,'b':2000,'c':3000}
    return render (request,'conditional.html',context=d)

def loop(request):
    d={'name':'venkat'}
    return render(request,'loop.html',context=d)