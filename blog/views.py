from django.http import HttpResponse, HttpResponseNotFound, \
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
# from datetime import datetime
# from django.template import Context
# from django.template.loader import get_template
# from django.core.mail import EmailMultiAlternatives
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

# import json
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, JsonResponse
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# from rest_framework import viewsets
# from rest_framework.viewsets import ModelViewSet

# from .serializers import*
# from .models import *
# from .forms import *

def blog_list(request):
    data = Blog.objects.all()
    return render(request, 'blog_list.html',{'m':data})

def index(request):
    data = Blog.objects.all()
    return render(request, 'index.html',{'m':data})

def blog_detail(request, **kwargs):
    pk = kwargs['pk']
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', {'documents': documents})


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

def loginv1(request):
    return render(request, 'loginv1.html')

# API 

def apitest(request):
    json_object = {'key': "value"}
    return JsonResponse(json_object)


class RapperViewSet(viewsets.ModelViewSet):
    queryset = Rapper.objects.all().order_by('aka')
    serializer_class = RapperSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer




def check_login(request):
    print("WOW")
	# if request.method == "POST":
	# 	username = request.POST.get("username", "")
	# 	password = request.POST.get("password", "")
    #     print(username)
    #     print(password)
    # else:
    #     print('fail')        
		# user = Tblusers.objects.using("user").filter(userid=username)
		# if user.count() > 0 :
		# 	pwd_encrypt = hashlib.md5( password.encode('utf-8') ).hexdigest()
		# 	# if user[0].password == pwd_encrypt:
		# 	if True:
		# 		# user_kpi = Employee.objects.filter(userid=username)
		# 		request.session['error'] = ""
		# 		request.session['username'] = username
		# 		if user_kpi.count() > 0:
		# 			emp = Employee.objects.get(userid=username)
		# 		else:
		# 			emp = Employee.objects.create(userid=username)
					
		# 		user = Tblusers.objects.using("user").get(userid=username)
		# 		department = user.department.split(' ',1)
		# 		cost = department[0]
		# 		dep = department[1] if len(department) > 1 else department[0]
		# 		user_dept = Department.objects.filter(department=dep)
		# 		if user_dept.count() > 0:
		# 			dep = Department.objects.get(department=dep)
		# 			print('get')
		# 		else:
		# 			dep = Department.objects.create(department=dep)
		# 			dep.directer = '13317'
		# 			dep.country = 'Thailand'
		# 			print('create')
		# 		dep.costcenter = cost
		# 		dep.save()
		# 		emp.department = dep
		# 		emp.prefix = user.prefixe
		# 		emp.first_name = user.firstnamee
		# 		emp.last_name = user.lastnamee
		# 		emp.logindate = datetime.datetime.now()
		# 		emp.email = user.email

		# 		emp.save()
		# 		# dep = Department.objects.get(department=dep)
		# 		return HttpResponseRedirect('/')
		# 	else:
		# 		error = "Password is Wrong!!!"
		# 		request.session['error'] = error
		# 		request.session[''] = error
		# 		messages.error(request, error)
		# 		return HttpResponseRedirect('/login')
		# else:
		# 	error = "Your account is Wrong!!!"
		# 	request.session['error'] = error
		# 	request.session[''] = error
		# 	messages.error(request, error)
		# 	return HttpResponseRedirect('/login')

def login(request):
	try:
		# request.session['username'] = '45446'
		username = request.session['username']
        # print("WOW")
		return HttpResponseRedirect('/')
	except Exception as e:
		return render(request, 'login_page.html')

def logout(request):
	del request.session['username']
	return HttpResponseRedirect('/login')
