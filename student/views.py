from django.shortcuts import render,redirect
from Account.models import Account
from django.contrib.auth.hashers import make_password
from new_lms.password import randomPassword
from new_lms.mail import Mail
from student.models import Student
from django.contrib import messages

# Create your views here.
def student_view(request):
    return render(request, 'student/dashboard.html')

def manager_studentview(request):
    if request.method == 'GET':
        return render(request,'manager/manager_studentview.html')
    else:
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = request.POST['contact']
        password = randomPassword()
        user = Account(email=email, password=make_password(password), is_teacher=False,is_manager=False,is_student=True)
        user.save()
        msg = f'{name}, your account is created successfully \n use the following credential to login \n email:{email} \n password:{password}'
        Mail(subject='Account created', message=msg,recipient_list=[email])
        student = Student(name=name, contact=contact, user_id=user.id)
        student.save()
        messages.add_message(request,messages.SUCCESS,'student Account is created successfully')
        return redirect('manager_view')