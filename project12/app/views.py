from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def EmployeeModelForm(request):
    EO=Employee.objects.all()
    d={'Employee':EO}
    
    return render(request,'EmployeeForm.html',d)
def insert_employeedata(request):
    if request.method=='POST':
        ename=request.POST['ename']
        mobile=request.POST['mobile']
        salary=request.POST['salary']
        dept=request.POST['dept']
        EO=Employee.objects.get_or_create(Ename=ename,mobile=mobile,salary=salary,dept=dept)[0]
        EO.save()
        return HttpResponse("employee data inserted")
    return render (request,'')