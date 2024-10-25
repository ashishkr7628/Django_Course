from django.http import HttpResponse
import datetime
from django.shortcuts import render

def test(request):
    isActive=False
    
    if request.method=="POST":
     check= request.POST['check']
     
     if check=='on': isActive=True
     else:isActive= False
     print(check)
    
    date= datetime.datetime.now()
   
    
    name="Ashish Kumar"
    
    list_of_programs=['WAP to check even or odd',
                      'WAP to check prime number',
                      'WAP to print all prime numbers from 1 to 100',
                      'WAP to print pascals triangle']
    
    print("test function is called from view")
    
    student={
        
        "student_name":"Rahul",
        "student_college": "ZYZ",
        "student_city":"LUCKNOW"
        
        
        
    }
    
    data={
        
        
        "date":date,
        "isActive":isActive,
        "name":name,
        "student":student,
        "list_of _all_programs":list_of_programs,
        
    }
    
    
    
#    return HttpResponse("<h1>Hello this is index page and </h1>"+str(date))






    return render(request,"home.html",data)
def about(request):
    # return HttpResponse("<h1> This is about page</h1>")
    return render(request,"about.html",{})
def services(request):
    # return HttpResponse("<h1> This is services page </h1>")
    return render(request,"services.html",{})