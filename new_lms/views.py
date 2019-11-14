from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from teacher.models import Teacher
from student.models import Student
from manager.models import Manager
def home(request):
    return render(request,'login.html')

def signin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('email')
        p = request.POST['password']
        user = authenticate(email=u, password=p)
        if user is not None:
            login(request, user)
            if request.user.is_manager:
                return redirect('manager_view')
            elif request.user.is_teacher:
                return redirect('teacher_view')
            elif request.user.is_student:
                return redirect('student_view')
            else:
                pass

        else:
            messages.error(request, 'Enter the valid username and password')
            return redirect('signin')

def changepassword(request):
    if request.method == 'GET':
        return render(request,'changepassword.html')
    else:
        if request.user.is_firstLogin:
            p1 = request.POST.get('password1')
            p2 = request.POST.get('password2')
            if p1 == p2:
                pass

def signout(request):
    logout(request)
    return redirect('signin')
