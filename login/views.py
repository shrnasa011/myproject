from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from compendia.models import *
#from Models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django import forms
from django.forms import ModelForm, PasswordInput, modelform_factory
from django.views import generic
# Create your views here.

class LoginForm(ModelForm):
    class Meta:
        model=MyUser
        fields=[ 'username', 'password']
        widgets={'user.password':PasswordInput}

class SignupForm(ModelForm):
    class Meta:
        model=MyUser
        fields=['username', 'password', 'email', 'first_name', 'last_name', 'contact', 'address',]
        widgets={'user.password':PasswordInput}


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        #check here
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:login'))
            #else:
                #Display error

    else:
        form=SignupForm()

    #Return to the same page
    return render(request, 'login/signup.html', {'form':form,})

    
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        #check here
        if form.is_valid():
            user=MyUser.objects.filter(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                request.session['user']=form.cleaned_data['username']
                return HttpResponseRedirect(reverse('compendia:index', ))
            else:
                return render(request, 'login/initial.html', {'form':form, 'error_message':"Invalid username or password",})

    else:
        form=LoginForm()

    #Return to the same page
    return render(request, 'login/initial.html', {'form':form,})
        

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request, 'login/logout.html')
