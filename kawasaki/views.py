from django.shortcuts import render,redirect
from kawasaki.models import Kawasaki
from kawasaki.forms import KawasakiForm
from authenticate import Authentication
# Create your views here.
@Authentication.valid_user
def index(request):
    print(request.method)
    if(request.method=="POST"):
        page=int(request.POST['page'])

        if('prev' in request.POST):
            page=page-1

        if('next' in request.POST):
            page=page+1

        tempOffSet=page-1
        offset=tempOffSet*4
        print(offset)

    else:
        offset=0
        page=1

    kawasaki=Kawasaki.objects.raw("select * from kawasaki limit 4 offset %s",[offset])
    pageItem=len(kawasaki)
    return render(request,"kawasaki/index.html",{'kawasaki':kawasaki,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=KawasakiForm(request.POST,request.FILES)
        form.save()
        return redirect("/kawasaki")
    else:
        form=KawasakiForm()
    return render(request,"kawasaki/create.html",{'form':form})

@Authentication.valid_user_where_id
def update(request,id):
    kawasaki=Kawasaki.objects.get(kawasaki_id=id)
    if request.method=="POST":
        form=KawasakiForm(request.POST,request.FILES,instance=kawasaki)
        form.save()
        return redirect("/kawasaki")
    else:
        form=KawasakiForm(instance=kawasaki)
    return render(request,"kawasaki/edit.html",{'form':form})

@Authentication.valid_user_where_id
def delete(request,id):
    kawasaki=Kawasaki.objects.get(kawasaki_id=id)
    kawasaki.delete()
    return redirect("/kawasaki")