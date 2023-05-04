from django.db import models

# Create your models here.
from django.db import models
import datetime
import os
from asyncio.windows_events import NULL
# Create your models here.

class user_type(models.Model):
     Usertype = models.CharField(max_length=50,default='')

class reg_tbl(models.Model):
     Name = models.CharField(max_length=50,default='')
     Dob = models.CharField(max_length=50,default='')
     Gender = models.CharField(max_length=50,default='') 
     Mobileno = models.CharField(max_length=50,default='')
     Email = models.CharField(max_length=50,default='',unique=True)
     Address=models.CharField(max_length=50,default='')
     Password = models.CharField(max_length=50,default='')
     Status = models.TextField(max_length=50,default='')
     Usertype = models.ForeignKey(user_type, on_delete=models.CASCADE,null=True)
     # Approve = models.CharField(max_length=50,default='')
     # Reject = models.CharField(max_length=50,default='')
     
# class ques_tbl(models.Model):
#      Question=models.CharField(max_length=200,default='',null=True)
#      Status = models.CharField(max_length=50,default='')
#      did = models.ForeignKey(reg_tbl,on_delete=models.CASCADE,null=True)



def nutrition1(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('screenshots/', filename)

class nutrition_tbl(models.Model):
     Title = models.TextField(max_length=200,default='')
     Description = models.CharField(max_length=500, null=True)
     Image = models.FileField(upload_to=nutrition1,max_length=500, default='')
     Time=models.TextField(max_length=200,default='')
     BP=models.TextField(max_length=200,default='')
     Cholesterol=models.TextField(max_length=200,default='')
     Diabetes=models.TextField(max_length=200,default='')
     Weight=models.TextField(max_length=200,default='')
     did = models.TextField(max_length=200,default='')

class quest_tbl(models.Model):
     Question=models.CharField(max_length=200,default='',null=True)
     Status = models.CharField(max_length=50,default='')
     did = models.ForeignKey(reg_tbl,on_delete=models.CASCADE,null=True)

class answer_tbl(models.Model):
     replay =models.TextField(max_length=200,default='')
     uid = models.TextField(max_length=200,default='')
     qid= models.ForeignKey(quest_tbl,on_delete=models.CASCADE,null=True)
     ans=models.TextField(max_length=200,default='')