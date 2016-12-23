from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course
# Create your views here.

def index(request):
    courses = Course.objects.all().order_by('-created_at')
    context = {
        'courses':courses,
    }
    return render(request, 'course_app/index.html',context)

def add_course(request):
    if request.method == "POST":
        print request.POST
        response = Course.objects.validate_course(name=request.POST['name'], description=request.POST['description'])
    if response[0]:
        messages.success(request,response)
    else:
        for error in response[1]:
            messages.error(request,error)
    return redirect('/')

def destroy_course(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course':course,
    }
    return render(request,'course_app/destroy.html',context)

def delete_course(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
