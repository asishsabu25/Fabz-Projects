from django.shortcuts import render
from django.conf import settings
from urllib import request
from django.shortcuts import render,redirect
from mediapp.models import *
#import os
import smtplib
from mediapp.models import *
from django.urls import reverse

# Create your views here.

def index(request): 
   a=user_type.objects.all()
   b=reg_tbl.objects.all()
   c=quest_tbl.objects.all()
   d=answer_tbl.objects.all()
   return render(request,'user/userindex.html',{'a':a,'b':b,'c':c,'d':d})

def home(request): 
   return render(request,'public/index.html')
        

def reg(request):
   if request.method=='POST':
      print('--------------------------')
      name = request.POST.get('name')
      dob=request.POST.get('dob')
      gender=request.POST.get('gender')
      mobileno=request.POST.get('mobileno')
      email=request.POST.get('email')
      address=request.POST.get('address')
      password=request.POST.get('password')
      cpass = request.POST.get('cpass')
      status=request.POST.get('status')
      usertype=request.POST.get('usertype')
      print(usertype)
      if password == cpass:
         data = reg_tbl.objects.create(Name=name,Usertype_id=int(usertype),Dob=dob,Gender=gender,Mobileno=mobileno,Email=email,Address=address,Password=password)
         return redirect('/login')
        
      else:
         a='password does not match'
         return render(request,'public/register.html',{'a':a})
      
   d=user_type.objects.filter()
   print(d)
   return render(request,'public/register.html',{'d': d})
    
   



def logout(request):
   request.session.flush()
   return redirect('/')
   
                   
             
             
           
             
       
def log(request):
   if request.method == 'POST':
      username = request.POST.get('email')
      password = request.POST.get('password')
      user=reg_tbl.objects.filter(Email=username,Password=password,Usertype=4,Status='complete').first()
      user1=reg_tbl.objects.filter(Email=username,Password=password,Usertype=4).first()
      if reg_tbl.objects.filter(  Email=username,Password=password):
         data = reg_tbl.objects.get(Email=username,Password=password)
         request.session['userid']=data.Usertype_id

            # request.session['usertype']=data.Usertype_id
         if data.Usertype_id == 1:
            request.session['adminid']=data.id
               #  request.session['aname']=data.Name
            return redirect('/adminindex')
         if data.Usertype_id == 2:
            user=data.Email
            upass=data.Password
            data2=reg_tbl.objects.get(Email=user,Password=upass)
            request.session['doctorid']=data2.id
               #  request.session['dname']=data2.Name
            return redirect('/doctorindex')
         if user:
            usr = data.Email
            upass = data.Password
            data3 = reg_tbl.objects.get(Email=usr,Password=upass)
            request.session['userid']=data3.id
               #  request.session['uname']=data3.Name
            return redirect('/userindex')
           
           
         if user1:
            usr = data.Email
            upass = data.Password
            data4 = reg_tbl.objects.get(Email=usr,Password=upass)
            request.session['userid']=data4.id
               #  request.session['uname']=data3.Name
            return redirect('/viewapproveqstn')
   return render(request,'public/login.html')
      #  if request.session.has_key('userid'):
      #    if request.session['usertype'] == 1:
      #       return redirect('/adminindex')
      #    elif request.session['usertype'] == 2:
      #       return redirect('/doctorindex')
      #    else:
      #       return redirect('/userindex')
      #  else:
      #   return render(request,'user/login.html')
           


def adminindex(request): 
   if request.session.has_key('adminid'):
    c = reg_tbl.objects.all()
    return render(request,'admin/adminindex.html',{'c':c})
   else:
        return redirect('/login')


def userindex(request):
    if request.session.has_key('userid'):
        c = reg_tbl.objects.all()
        return render(request,'user/userindex.html',{'c':c})
    else:
        return redirect('/login')


def doctorindex(request): 
    if request.session.has_key('doctorid'):
      c = reg_tbl.objects.all()
      # obj=reg_tbl.objects.filter(Usertype_id=request.['doctorid']).first()
      # print(obj)
      return render(request,'doctor/doctorindex.html',{'c':c})

    else:
        return redirect('/login')
       

   



def viewdoctor(request):
   b=reg_tbl.objects.filter(Usertype_id=2).all()
   return render(request,'admin/viewdoctors.html',{'b':b})

def viewtrainee(request):
   b=reg_tbl.objects.filter(Usertype_id=3).all()
   return render(request,'admin/viewtrainees.html',{'b':b})


def approve(request,id):
   b = reg_tbl.objects.get(id=id)
   # if (a.Approve =="Approve"):
   b.Status = "Approved"
   mail = smtplib.SMTP('smtp.gmail.com', 587)
   mail.ehlo()
   mail.starttls()
   # mail.login(settings.Email_HOST_USER, settings.Email_HOST_PASSWORD)
   message = "Your Registeration is Approved Successfully"
   # Email = b.Email
   # mail.sendmail(settings.Email_HOST_USER, Email, message)
   b.save() 
   return redirect('/viewdoctors') 

# def reject(request,id):
#    b = reg_tbl.objects.get(id=id)
#    # if(a.Reject == "Reject"):
#    b.Reject = "Rejected"
#    b.Approve = "Approve"
#    mail = smtplib.SMTP('smtp.gmail.com', 587)
#    mail.ehlo()
#    mail.starttls()
#    mail.login(settings.Email_HOST_USER, settings.Email_HOST_PASSWORD)
#    message = "Your Registeration is Rejected !"
#    Email = b.Email
#    mail.sendmail(settings.Email_HOST_USER, Email, message)
#    b.save() 
#    return redirect('/viewdoctors')   
#    # return render(request,'admin/viewstudents.html')   

# def addquestion(request,id):
#    q=ques_tbl.objects.get(id=id)
#    qid=q.id
#    did=request.session['doctorid']
#    dname=request.session['dname']
#    if request.method == 'POST':
#       data=reg_tbl.objects.get(did=did,dname=dname,qid=qid)
#       return redirect('/addquestion')



# def login(request):
#    if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         if reg_tbl.objects.filter(  Email=username,Password=password):
#             data = reg_tbl.objects.get(Email=username,Password=password)
#             request.session['userid']=data.id
#             request.session['usertype']=data.Usertype_id
#         if data.usertype ==1:
#           return redirect('/adminindex')
#    return render(request,'user/login.html')\


          
def addquestion(request):
   if request.method == 'POST':
   #   d=request.session['doctorid']
   #   udet=reg_tbl.objects.filter(id=d)
     question=request.POST.get('question')
     did=request.POST.get('did')
     print(request.session['doctorid'])
     a=request.session['doctorid']
     udet=reg_tbl.objects.get(id=a)
     print(udet)
     did=udet.id
   #   print(did)
   #   print(did)
     data=quest_tbl.objects.create(Question=question,did_id=did)
   return render(request,'doctor/addquestion.html')

def viewquesadmin(request):
   q=quest_tbl.objects.all()
   return render(request,'admin/viewquestionadmin.html',{'q':q})

def approveadmin(request,id):
   q = quest_tbl.objects.get(id=id)
   # if (a.Approve =="Approve"):
   q.Status = "Approved"
   mail = smtplib.SMTP('smtp.gmail.com', 587)
   mail.ehlo()
   mail.starttls()
   # mail.login(settings.Email_HOST_USER, settings.Email_HOST_PASSWORD)
   message = "Your Question is Approved Successfully"
   # Email = q.Email
   # mail.sendmail(settings.Email_HOST_USER, Email, message)
   q.save() 
   return redirect('/viewquestionadmin') 



# def viewapproveqstn(request):
#    if request.method == 'POST':
#       replay = request.POST.get('replay')
#       qid=request.POST.get('qid')
#       uid=request.POST.get('uid')
#       a=request.session['userid']
#       udet=reg_tbl.objects.get(id=a)
#       uid=udet.id
#       data = ans_tbl.objects.create(Replay=replay,qid_id=qid,uid=uid)
#       q=ques_tbl.objects.filter(Status='Approved').all()
#    return render(request,'user/viewapproveqstns.html',{'q':q})       


def viewapproveqstn(request):
   qstn=quest_tbl.objects.filter(Status='Approved').all()
   c=reg_tbl.objects.get(id=request.session['userid'])
   # c=quest_tbl.objects.filter(Status='Approved').all()
   if request.method == 'POST':

      # b=reg_tbl.objects.all()
      for i in qstn:
         replay = request.POST.get('replay_'+str(i.id)) 
            # uid=request.POST.get('uid') 
         qid=i.id
         data = answer_tbl.objects.create(replay=replay,qid_id=qid, uid=c.id)
         c.Status='complete'
         c.save()
         d=answer_tbl.all()
         for i in d:
            if qid.Question =="BP":
               if i.replay>80:
                  i.ans="HIGH"
               else:
                  i.ans="LOW"
            elif i.qid.Question == "Cholesterol":
               if i.replay>80:
                  i.ans="HIGH"
               else:
                  i.ans="LOW"
            elif i.qid.Question == "Diabetes":
               if i.replay>80:
                  i.ans="HIGH"
               else:
                  i.ans="LOW"
            elif i.qid.Question == "Weight":
               if i.replay>80:
                  i.ans="HIGH"
               else:
                  i.ans="LOW"
            else:
               i.ans="invalid"
   return render(request,'user/viewapproveqstns.html',{'qstn':qstn,'c':c})



def addnutrition(request):
   if request.method == 'POST':
      title=request.POST.get('title')
      time=request.POST.get('time')
      image=request.FILES.get('image')
      description=request.POST.get('description')
      bp=request.POST.get('bp')
      cholesterol=request.POST.get('cholesterol')
      diabetes=request.POST.get('diabetes')
      weight=request.POST.get('weight')
      b=request.session['doctorid']
      udet=quest_tbl.objects.get(id=b)
      did=udet.id
      data=nutrition_tbl.objects.create(Title=title,Image=image,Description=description,BP=bp, Cholesterol= cholesterol, Diabetes=diabetes,Weight=weight,did=did,Time=time)
   return render(request,'doctor/addnutrition.html')

def viewnutrition(request):
   n=nutrition_tbl.objects.all()
   d=answer_tbl.objects.all()  
   return render(request,'user/viewnutrition.html',{'n':n,'d':d})
# Create your views here.
