from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Employee
# Create your views here.
# def home(request):
#     return render(request, 'index.html')

def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html",{'allemployees':emp})

def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")

def addemployee(request):
    if request.method == "POST":
        # Take all the parameters from the form. by their names kept
        employeeid = request.POST.get('employeid')
        employeename = request.POST.get('employeename')
        employeeeemail = request.POST.get('employeeemail')
        employeeaddress = request.POST.get('employeeaddress')
        employeephone = request.POST.get('employeephone')
    
        # create an object of the Employee model
        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeeeemail
        e.address = employeeaddress
        e.phone = employeephone
        e.save()
        return redirect("/allemployees")
        
    return render(request, "emp/addemployee.html")