from django.shortcuts import render,redirect
from new_lms.password import randomPassword
from Account.models import Account
from django.contrib.auth.hashers import make_password
from teacher.models import Teacher
from new_lms.mail import Mail
from django.contrib import messages


def manager_view(request):
    return render(request, 'manager/dashboard.html')

def manager_teacherview(request):
    if request.method=='GET':
        return render(request,'manager/manager_teacherview.html')
    else:
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = request.POST['contact']
        password = randomPassword()
        user = Account(email=email, password=make_password(password), is_teacher=True,is_manager=False,is_student=False)
        user.save()
        msg = f'{name}, your account is created successfully \n use the following credential to login \n email:{email} \n password:{password}'
        Mail(subject='Account created', message=msg, recipient_list=[email])
        teacher = Teacher(name=name, contact=contact, user_id=user.id)
        teacher.save()
        messages.add_message(request,messages.SUCCESS,'Teacher Account is created successfully')
        return redirect('manager_teacherview')
