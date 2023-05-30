from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def demo_all(request):
    data=User.objects.all()
    # print(data)
    return render(request,'table.html',{'abc':data})

def demo_filter(request):
    data=User.objects.filter(email="demo@gmail.com")
    # print(data)
    return render(request,'table.html',{'abc':data})
def demo_get(request):
    data=User.objects.get(username="test")
    # print(data)
    return render(request,'table_get.html',{'abc':data})


def login(request):
    if request.method=="POST":
        try:
            data=User.objects.get(email=request.POST['email'],password=request.POST['Password'])
            if data:
                request.session['email']=data.email
                return redirect('index')
            else:
                return render(request,'login.html',{'message':'Invalid Email Or Password'})
        except:
                return render(request,'login.html',{'message':'Invalid Email Or Password'})

    return render(request,'login.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('login')
    else:
        return redirect('login')

def index(request):
    if 'email' in request.session:
        a=request.session['email']
        data=Category.objects.all()
        return render(request,'index.html',{'abc':data,'a':a})
    else:
        data=Category.objects.all()
        return render(request,'index.html',{'abc':data})



def productall(request):
    data=Product.objects.all()
    return render(request,'productall.html',{'abc':data})


def product_categorywise(request,id):
    data=Product.objects.filter(productcategory=id)
    return render(request,'productall.html',{'abc':data})


def product_get(request,id):
    data=Product.objects.get(id=id)
    return render(request,'singleproduct.html',{'abc':data})

def register(request):
    if request.method=='POST':
        name1=request.POST['name']
        email1=request.POST['email']
        phone1=request.POST['phone']
        password1=request.POST['password']
        data=User()
        data.username=name1
        data.email=email1
        data.phone=phone1
        data.password=password1
        a=User.objects.filter(email=email1)
        if len(a)==0:
            data.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'message':"user alredy exist"})

    return render(request,'register.html')