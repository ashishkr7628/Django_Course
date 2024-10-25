from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from .forms import FeedbackForm

from .models import Emp,Testimonial


# Create your views here.


def emp_home(request):

    emps = Emp.objects.all()
    print(emps)

    return render(request, "emp/home.html", {"emps": emps})


def add_emp(request):
    if request.method == "POST":

        name = request.POST.get("emp_name")
        id = request.POST.get("emp_id")
        address = request.POST.get("emp_address")
        phone = request.POST.get("emp_phone")
        working = request.POST.get("emp_working")
        dept = request.POST.get("emp_dept")

        print(name)
        print(id)
        print(address)
        print(working)
        print(phone)
        print(dept)

        emp = Emp()

        emp.name = name
        emp.emp_id = id
        emp.address = address
        emp.working = working
        emp.department = dept
        emp.phone = phone

        if emp.working is None:
            emp.working = False
        else:
            emp.working = True

        emp.save()

        return redirect("home")

    return render(request, "emp/add-emp.html")


def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()

    return redirect("home")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update-emp.html",{"emp":emp})

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp=Emp.objects.get(pk=emp_id)
        
        name = request.POST.get("emp_name")
        id = request.POST.get("emp_id")
        address = request.POST.get("emp_address")
        phone = request.POST.get("emp_phone")
        working = request.POST.get("emp_working")
        dept = request.POST.get("emp_dept")
        
        
        emp.name = name
        emp.emp_id = id
        emp.address = address
        emp.working = working
        emp.department = dept
        emp.phone = phone
        
        emp.save()
        
        return redirect("home")
def testimonials(request):
    
    tests= Testimonial.objects.all()
    
    
    return render(request,"emp/testimonials.html",{"tests":tests})

def feedback(request):
    
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data["email"])
            print(form.cleaned_data["name"])
            print(form.cleaned_data["feedback"])
            
    else: 
        form=FeedbackForm()
    return render(request,"emp/feedback.html",{"form":form})

