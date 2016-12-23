from django.shortcuts import render,HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('<h1>we made it</h1>')
    return render(request, 'disappearingninjas/index.html')

def display_all(request):
    return render(request, 'disappearingninjas/ninja.html')

def display_color(request, color):
    if color == "blue" or color == "orange" or color == "purple" or color == "red":
        context = {
            'color' : color
        }
    else:
        context = {
            'color' : 'megan_fox'
        }
    return render(request, 'disappearingninjas/ninja_color.html',context)
