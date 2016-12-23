from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    if 'submit_num' not in request.session:
        request.session['submit_num'] = 0
    return render(request,'surveyform/index.html')

def process(request):
    if 'submit_num' in request.session:
        request.session['submit_num'] += 1
        context = {
            'name' : request.POST['name'],
            'location' : request.POST['location'],
            'language' : request.POST['language'],
            'comment' : request.POST['comment']
        }
        return render(request, 'surveyform/results.html',context)
    else:
        return redirect('/')
