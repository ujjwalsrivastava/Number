from django.shortcuts import render,redirect 
import requests
from .models import *
from django.http import FileResponse,HttpResponse
from .forms import *


def send_file(request):
    
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse('successfully uploaded')
    else: 
        form = ImageForm() 
    return render(request, 'kl.htm', {'form' : form}) 

def watch(request):
    gh=Number_store.objects.all()
    return render(request,'ik.htm',{'value':gh})

def Take_num(request):
    if request.method=='POST':
        num=request.POST['num']
        topic=request.POST['topic']
        Number_store(num=num, topic=topic).save()

        #Giving below Query to Fetch Data
        results = Number_store.objects.all()
    
        return render(request,'ok.htm',{'value':'Submitted','result':results})
    else:
        return render(request,'ok.htm')







def Audio_store(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse('successfully uploaded')
    else: 
        form = AudioForm() 
    return render(request, 'aud.htm', {'form' : form}) 

def Audio_get(request):
    vt=Audio_storee.objects.all()
    return render(request,'aud1.htm',{'vt':vt})
