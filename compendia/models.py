from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

import datetime

class Hospital(models.Model):

    hospital = models.OneToOneField(User)
    join_date = models.DateTimeField('Date of joining')
    # username, first_name, last_name, email, password, last_login

    def __str__(self):
        return self.hospital.username

class Doctor(models.Model):

    doctor = models.OneToOneField(User)
    join_date = models.DateTimeField('Date of joining')
    contact = models.CharField(max_length=11)
    room_no = models.CharField(max_length=50)

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    # username, first_name, last_name, email, password, last_login

    def __str__(self):
        return self.doctor.username

class MyUser(models.Model):
	
    user = models.OneToOneField(User)
    # username, first_name, last_name, email, password, last_login
    join_date = models.DateTimeField('Date of joining')
    contact = models.CharField(max_length=11)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    ask_date = models.DateTimeField('Date when appointment is requested')
    acc_date = models.DateTimeField('Date when appointment request is accepted')
    app_date = models.DateTimeField('Date of appointment')

    def __str__(self):
        return self.user.username

    def was_accepted_recently(self):
    	now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now

    def was_asked_recently(self):
    	now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now

    was_accepted_recently.admin_order_field = 'acc_date'
    was_accepted_recently.boolean = True

    was_asked_recently.admin_order_field = 'ask_date'
    was_asked_recently.boolean = True

    def about_to_come(self):
    	now = timezone.now()
    	return now <= self.app_date <= now + datetime.timedelta(days=7)
    
    about_to_come.admin_order_field = 'app_date'
    about_to_come.boolean = True
    


class Prescription(models.Model):

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    pre_date = models.DateTimeField('Date of prescription')
    pre_text = models.TextField(max_length=250)

    def __str__(self):
        return self.pre_text

    def was_prescribed_recently(self):
    	now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.pub_date <= now
    
    was_prescribed_recently.admin_order_field = 'pre_date'
    was_prescribed_recently.boolean = True

class Prescribed_Medicines(models.Model):

    user = models.ForeignKey(Prescription, on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    pre_medicine = models.TextField(max_length=100)
    pre_duration = models.IntegerField()
    pre_freq = models.TextField(max_length=10)

    def __str__(self):
        return self.pre_medicine
