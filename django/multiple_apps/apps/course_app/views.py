from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Enrolled
from ..login_reg.models import User
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    if 'id' in request.session:
        courses = Course.objects.all().order_by('-created_at')
        context = {
            'courses':courses,
        }
        return render(request, 'course_app/index.html',context)
    else:
        return redirect(reverse('login_reg:index'))

def add_course(request):
    if request.method == "POST":
        # print request.POST
        response = Course.objects.validate_course(name=request.POST['name'], description=request.POST['description'])
    if response[0]:
        messages.success(request,"Succesfully added a course!")
    else:
        for error in response[1]:
            messages.error(request,error)
    # return redirect('/')
    return redirect(reverse('course_app:index'))

def destroy_course(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course':course,
    }
    return render(request,'course_app/destroy.html',context)
    # return redirect(reverse('course_app:delete_course',kwargs={'course':course,}))

def enrolled(request):
    if 'id' in request.session:
        context = {
            'courses' : Course.objects.all(),
            'users' : User.objects.all(),
            'enrolled' : Enrolled.objects.class_size(),
            'test' : Enrolled.objects.all(),
        }
        # test = Enrolled.objects.all().values('course').annotate(num_students=Count('user'))
        # print test.query
        return render(request, 'course_app/enrolled.html',context)
    else:
        return redirect(reverse('login_reg:index'))

def add_enrolled(request):
    if request.method == "POST":
        response = Enrolled.objects.enroll_user(user=request.POST['user'],course=request.POST['course'])
        if response[0]:
            # print response[1]
            messages.success(request,"Successfully added " + str(response[1].user.first_name) + " to course " + str(response[1].course.name))
            return redirect(reverse('course_app:enrolled'))
        else:
            for error in response[1]:
                messages.error(request,error)
            return redirect(reverse('course_app:enrolled'))
    else:
        return redirect(reverse('course_app:enrolled'))

def delete_course(request, id):
    Course.objects.get(id=id).delete()
    # return redirect('/')
    return redirect(reverse('course_app:index'))
