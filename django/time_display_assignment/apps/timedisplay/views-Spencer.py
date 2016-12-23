from django.shortcuts import render, HttpResponse
from time import strftime
from datetime import datetime

# Create your views here.

def index(request):
    context = {
    "timekey":str(datetime.now().strftime("%b %d, %Y %I:%M %p"))
    }
    return render(request,'timedisplay/index.html',context)
