from django.shortcuts import render,redirect
from order.models import Order
from order.forms import OrderForm
from authenticate import Authentication
# Create your views here.
#@Authentication.valid_user
def index(request):
    order=Order.objects.all()
    print(order)
    return render(request,'order/index.html',{'order':order})

#@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=OrderForm(request.POST,request.FILES)
        form.save()
        return redirect("/order")
    else:
        form=OrderForm()
    return render(request,"order/create.html",{'form':form})
