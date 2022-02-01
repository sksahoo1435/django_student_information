from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.


#This function add and show the items
def add_show(request):
    usr = User.objects.all()
    if request.method == 'POST':    
        fm = StudentRegistration(request.POST)
         
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password =pw)
            reg.save()
            fm = StudentRegistration()

    else: 
        fm = StudentRegistration()   
    return render(request, "enroll/addandshow.html",{'form':fm,'usr':usr})


#this function delete items
def delete_data(request,id):
    if request.method == 'POST':
        d = User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')

#This function EDIT the student information

def edit_data(request,id):
    if request.method == 'POST':
        up = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance = up)
        if fm.is_valid():
            fm.save()
    else:
        up = User.objects.get(pk = id)
        fm = StudentRegistration(instance = up)
    return render(request, 'enroll/update_student.html',{'form':fm})
