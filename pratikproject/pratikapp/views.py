from django.shortcuts import render
from django.contrib.auth.decorators  import login_required
from .  import forms
from django.http import HttpResponseRedirect
from pratikapp.models import Task


# Create your views here.


def home(request):
    return render(request,'pratikapp/home.html')

def logout(request):
    return render(request,'pratikapp/logout.html')

def signup(request):
    form=forms.SignupForm()
    if request.method=='POST':

        form=forms.SignupForm(request.POST)
        User=form.save()
        User.set_password(User.password)
        User.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request,'pratikapp/signup.html',{'form':form})

@login_required
def tasklist(request):
    tasklist=Task.objects.all()
    return render(request,'pratikapp/activityfeed.html',{'tasklist':tasklist})


@login_required
def createtask(request):
    form=forms.TaskForm()
    if request.method=='POST':
        form=forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    return render(request,'pratikapp/createtask.html',{'form':form})

def delete_view(request,id):
    tasklist=Task.objects.get(id=id)
    tasklist.delete()
    return HttpResponseRedirect('/')

def update_view(request,id):
    tasklist=Task.objects.get(id=id)
    if request.method=='POST':
        form=forms.TaskForm(request.POST,instance=tasklist)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'pratikapp/update_view.html',{'tasklist':tasklist})
