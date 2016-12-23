from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    #check if logged in
    if 'id' in request.session:
        try:
            # user_name = User.objects.get(id=request.session['id']).first_name
            # return render(request, 'login_reg/index.html',{'user':user_name,})
            return redirect(reverse('course_app:index'))
        except ObjectDoesNotExist:
            return render(request, 'login_reg/index.html')
    else:
        return render(request, 'login_reg/index.html')

def register_user(request):
    if request.method == "POST":
        print "registering user"
        #clean this up...
        response = User.objects.validate_registration(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email_address=request.POST['email_address'],password=request.POST['password'],confirm_password=request.POST['confirm_password'])
        if response[0]:
            #pass information to our partials form and load
            # messages.success(request,'Succesfully registered as a new user (and logged in)!')
            if 'id' not in request.session:
                request.session['id'] = response[1].id
            # return redirect(reverse('login_reg:index'))
            return redirect(reverse('course_app:index'))
        else:
            for error in response[1]:
                messages.error(request, error)
            # here we could just do a redirect('/') but if we want to pass back some values so the user does not need to re-enter them then we have to do the below
            context = {
                'first_name':request.POST['first_name'],
                'last_name':request.POST['last_name'],
                'email_address':request.POST['email_address'],
            }
            return render(request,'login_reg/index.html',context)
            # return redirect(reverse('login_reg:index'))
    else:
        return redirect(reverse('login_reg:index'))

def login_user(request):
    #verify not already logged in
    if 'id' not in request.session:
        response = User.objects.validate_login(email_address=request.POST['login_email'],password=request.POST['login_password'])
        if response[0]:
            # messages.success(request,'Succesfully logged in, Welcome back!!')
            if 'id' not in request.session:
                request.session['id'] = response[1].id
            # return redirect(reverse('login_reg:index'))
            return redirect(reverse('course_app:index'))
        else:
            for error in response[1]:
                messages.error(request, error)
            return redirect(reverse('login_reg:index'))
    else:
        #just so we don't crash our server...
        return redirect(reverse('login_reg:index'))


def logout_user(request):
    #logout...
    if 'id' in request.session:
        print "popping session"
        del request.session['id']
    return redirect(reverse('login_reg:index'))
