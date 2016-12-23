from django.shortcuts import render, HttpResponse
from .models import People
# Create your views here.
def index(request):
    People.objects.create(first_name="Spencer", last_name="Larsen")
    people = People.objects.all()
    print (people)
    return render(request,'third_app/index.html')
