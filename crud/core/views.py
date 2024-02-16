from django.shortcuts import render,redirect
from .forms import HomeForm
from .models import Model

# Create your views here.


def home(request):
    # hf = HomeForm()
    if request.method =="POST":
        hf = HomeForm(request.POST)
        if hf.is_valid():
            hf.save()
        mm = Model.objects.all()
        hf = HomeForm()
    else:
        mm = Model.objects.all()
        hf = HomeForm()        
    return render(request,'core/home.html',{"hf":hf,"mm":mm})

def delete(request,id):
    if request.method == "POST":
        de = Model.objects.get(pk=id)
        de.delete()
    return redirect('/home/')
