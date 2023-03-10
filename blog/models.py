from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date  = models.DateTimeField(auto_now_add=True)
    body  = models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    release_date = models.DateField()
    def __str__(self):
        return self.name


class Company_Category(models.Model):
    Company = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.Company)  


class Document(models.Model):
    docid = models.CharField(max_length=255, blank=True)
    Martril = models.CharField(max_length=255, blank=True)
    docdata = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % (self.docid)  

class UserID(models.Model):
    userid = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True, null=True) 
    fristname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    lastlogin = models.CharField(max_length=25, blank=True, null=True)
    profile = models.FileField(upload_to='documents/',default='', blank=True, null=True)
    def __str__(self):
        return '%s' % (self.userid)  

class Rapper(models.Model):
    name = models.CharField(max_length=100)
    aka = models.CharField(max_length=60)
    def __str__(self):
        return self.aka

class Personal_data(models.Model):
    personalid = models.CharField(max_length=50, blank=True)
    fristname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=25, blank=True)
    def __str__(self):
        return '%s' % (self.personalid)




