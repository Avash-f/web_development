from django.shortcuts import render,redirect
from kawasaki.models import Kawasaki
from customer.forms import CustomerForm
# Create your views here.
def index(request):
    kawasaki=Kawasaki.objects.all()
    return render(request,'home/index.html' ,{'kawasaki':kawasaki})

def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        result=form.save()
        request.session['customer_id']=result.customer_id
        return redirect("/")
    else:
        form=CustomerForm()
    return render(request,"home/register.html",{'form':form})

def login(request):

    if(request.method=='POST'):
       request.session['email']=request.POST['email']
       request.session['password']=request.POST['password']

       return redirect("/user")
    return render(request,"home/login.html")


def logout(request):
    request.session.clear()
    return redirect("/login")

def about(request):
    kawasaki=Kawasaki.objects.all()
    return render(request,'home/about.html' ,{'kawasaki':kawasaki})
def blog(request):
    kawasaki=Kawasaki.objects.all()
    return render(request,'home/blog.html' ,{'kawasaki':kawasaki})
def blog_details(request):
    kawasaki=Kawasaki.objects.all()
    return render(request,'home/blog-details.html' ,{'kawasaki':kawasaki})
def car(request):
    kawasaki=Kawasaki.objects.all()
    return render(request,'home/car.html' ,{'kawasaki':kawasaki})
def car_details(request):
    kawasaki=Kawasaki.objects.all()
    return render(request,'home/car-details.html' ,{'kawasaki':kawasaki})
def contact(request):
    kawasaki=Kawasaki.objects.all()
    return render(request,'home/contact.html' ,{'kawasaki':kawasaki})