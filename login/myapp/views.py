from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from .forms import RegisterForm
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password ,check_password
from django.db.models import Q
from django.core.exceptions import ValidationError
# Create your views here.

def index(request):   
    student=Register.objects.all()
    context ={
        'student':student,
        'message':"Viewing all student"
    }
    return render(request,'myapp/index.html',context=context)


def login(request):
    if request.method=='POST':
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        name=request.POST['name']
        last_name=request.POST['last_name']
        cfmpwd=request.POST['cfmpwd']
        image=request.FILES['image']
        if password==cfmpwd:
            password=make_password(password)
            user=Register(name=name,last_name=last_name,email=email,mobile=mobile,password=password,image=image)
            user.save()
            return redirect('index')
        else:
            raise ValidationError("Confirm Password does not match")
    return render(request,'myapp/login.html')

def update(request, s_id=0):
    if s_id:
        student=Register.objects.get(id=s_id)
        context={
            'student': student,
            'toast':False
        }
        return render(request,'myapp/update.html',context=context)
def makeupdate(request,s_id=0):
    student=Register.objects.get(id=s_id)
    context={
        'student': student,
        'toast':True,
        'message':'update unsuccessfull'
    }
    if request.method=='POST' and s_id:
        mobile=request.POST['mobile']
        password=request.POST['password']
        name=request.POST['name']
        last_name=request.POST['last_name']
        image=request.FILES['image']
        check = get_object_or_404(Register, id=s_id)
        if check_password(password,check.password): 
            check.name=name
            check.last_name=last_name
            check.mobile=mobile
            check.image=image
            check.save()
            student=Register.objects.all()
            context={
                'message':'Updated Successfully',
                'student':student
            }
            return render(request,'myapp/index.html',context)
    return render(request,'myapp/update.html',context)
        
def delete(request,s_id=0):
    if s_id and request.method=='POST':
        password=request.POST['password']
        user=Register.objects.get(id=s_id)
        if check_password(password,user.password):
                user.delete()
                messages.success(request,'Student Deleted Succesfully')
                return redirect('index')
        context={
        'student': user,
        'toast':True,
        'message':'Delete unsuccessfull'
    }
        return render(request,'myapp/update.html',context)


def view(request,slug):
    context={
        'Table':False
    }
    if slug=="first-name":
        if request.method=="POST":
            query=request.POST['name']
            users = Register.objects.filter(Q(name__icontains=query)) 
            context={
                'users':users,
                'table':True,
                'message':'Getting Student By first name'
            }
        return render(request,'myapp/view.html',context)
    elif slug=="last-name":
        if request.method=="POST":
            query=request.POST['name']
            users = Register.objects.filter(Q(last_name__icontains=query)) 
            context={
                'users':users,
                'table':True,
                'message':'Getting Student By Last name'
            }
        return render(request,'myapp/view.html',context)
        
    elif slug=="email":
        if request.method=="POST":
            query=request.POST['name']
            users = Register.objects.filter(Q(email__icontains=query)) 
            context={
                'users':users,
                'table':True,
                'message':'Getting Student By E-mail'
            }
        return render(request,'myapp/view.html',context)
    return render(request,'myapp/view.html',context)