from django.shortcuts import render, HttpResponse
#Controller!!!!
def index(request):
    response = "hello, I am your first request"
    # return HttpResponse(response)
    return render(request, "templates/first_app/index.html")

# Create your views here.
