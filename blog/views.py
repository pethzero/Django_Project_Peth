from django.http import HttpResponse,JsonResponse, HttpResponseNotFound, \
                                                HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import  transaction
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from .models import *
from .forms  import *
import datetime
import re
from django.contrib import messages
import time
import os
import hashlib
import json
import base64
import arrow
import csv
import pandas as pd
import simplejson
import sys

from django.core.cache import cache
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string
from pathlib import Path
from email.mime.image import MIMEImage
from datetime import timedelta


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
# from pyrfc import Connection
from django.http import HttpResponse, Http404

def home(request):
    try:
        username = request.session['username']
        user = UserID.objects.get(userid=username)
        documents = Document.objects.all()

    except Exception as e:
        return HttpResponseRedirect('/login')    
    param = {
        'user' : user,
        'documents': documents
    }
    return render(request, 'home.html',param)


def blog_list(request):
    data = Blog.objects.all()
    return render(request, 'blog_list.html',{'m':data})


def blog_detail(request, **kwargs):
    pk = kwargs['pk']
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html',
         {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Wow")
            return redirect('home')
    else:
        form = DocumentForm()
        print("...")
    return render(request, 'model_form_upload.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')

# API 
def test_api(request):
    data = Blog.objects.all()
    return render(request, 'test_api.html',{'m':data})

def apitest(request):
    json_object = {'key': "api_test"}
    return JsonResponse(json_object)


class RapperViewSet(viewsets.ModelViewSet):
    queryset = Rapper.objects.all().order_by('aka')
    serializer_class = RapperSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer




def check_login(request):
    username = request.POST.get('username',"")
    password = request.POST.get('password',"")
    try:
     
        user_person = UserID.objects.filter(userid=username)
        print("get user_person:",user_person)

        if user_person.exists():
                # if user[0].password == pwd_encrypt:
                if user_person[0].password == password:
                    user_person = UserID.objects.get(userid=username)
                    user_person.lastlogin = arrow.now().format('YYYY-MM-DD HH:mm:ss')
                    user_person.save()
                else:
                    error = "Your password is invalid !"
                    messages.error(request, error)
                    print(error)
                    return HttpResponseRedirect('/login/') 
        else:
            error = "Your username is invalid !"
            messages.error(request, error)
            print(error)
            return HttpResponseRedirect('/login/') 

        request.session['username'] = username 
        return HttpResponseRedirect('/')    

    except Exception as e:
        # print(e)
        print("{0} : {1}".format(sys.exc_info()[-1].tb_lineno,str(e)))
        error = "Your account is invalid !"
        print(error)
        messages.error(request, error)
        return HttpResponseRedirect('/login/')
          

    data = {
        'user' : username,
        'passowrd': password
    }
    return HttpResponse(simplejson.dumps(data,default=str), {'ContentType':'application/json'} )
        
# def loginv1(request):
#     return render(request, 'loginv1.html')
    

def login(request):
	try:
		username = request.session['username'] 
		return HttpResponseRedirect('/') 
	except Exception as e:
		print(e)
	return render(request, 'login.html') 

def logout(request):
	try:
		del request.session['username']
	except Exception as e:
		print(e)
	return HttpResponseRedirect('/login/') 