from enum import unique
from elaw import db,app,login_manager
from flask_login import UserMixin
from flask_table import Table, Col, LinkCol


@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))



class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200),default='')
    contact = db.Column(db.String(200),default='')
    approve = db.Column(db.String(200),default='')
    reject = db.Column(db.String(200),default='')
    status = db.Column(db.String(200),default='')
    address = db.Column(db.String(200),default='')
    place = db.Column(db.String(200),default='')
    type = db.Column(db.String(200),default='')
    court = db.Column(db.String(200),default='')
    barcodeid = db.Column(db.String(200),default='')
    qualification = db.Column(db.String(200),default='')
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    location=db.Column(db.String(200),default='')








class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    email= db.Column(db.VARCHAR)
    subject = db.Column(db.String(200))
    message= db.Column(db.String(200))
    usertype = db.Column(db.String(80), nullable=False)



class Law(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    law = db.Column(db.String(200))
    details= db.Column(db.VARCHAR)



class Court(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    court = db.Column(db.String(200))
    jury = db.Column(db.String(200))
    address= db.Column(db.String(200))
    location=db.Column(db.String(200))
    time=db.Column(db.String(200))



class Case(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    lid = db.Column(db.String(200))
    case = db.Column(db.String(200))
    desc = db.Column(db.String(200))
 






class BookLawyer(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(80))
    lid = db.Column(db.String(80), nullable=False)
    uname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(200))
    ucontact = db.Column(db.String(200))
    lcontact = db.Column(db.String(200))
    uemail = db.Column(db.String(200))
    lemail = db.Column(db.String(200))
    address = db.Column(db.String(200))
    place = db.Column(db.String(200))
    pstatus=db.Column(db.String(200))
    status=db.Column(db.String(200))
    approve = db.Column(db.String(200))
    reject = db.Column(db.String(200))
    case = db.Column(db.String(200))
    cardno = db.Column(db.String(200))
    cvv = db.Column(db.String(200))
    month = db.Column(db.String(200))
    year = db.Column(db.String(200))
    amount = db.Column(db.String(200))
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    buk_date = db.Column(db.String(200))
    noti_msg=db.Column(db.String(200))
    st=db.Column(db.String(200))


class announcement(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ann = db.Column(db.String(200))
    details= db.Column(db.VARCHAR)

class rules(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rules = db.Column(db.String(200))
    details= db.Column(db.VARCHAR)

class caserecords(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    records = db.Column(db.String(200))
    description= db.Column(db.VARCHAR)

class jurys(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    juryname = db.Column(db.String(200))
    details= db.Column(db.VARCHAR)
    qualification = db.Column(db.VARCHAR)
    experience = db.Column(db.String(2))
    specialization = db.Column(db.VARCHAR)
    court = db.Column(db.String(200))