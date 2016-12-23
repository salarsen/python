from django.shortcuts import render, HttpResponse
import random
import datetime
# Create your views here.

def index(request):
    if 'goldcount' not in request.session or 'activities' not in request.session:
        request.session['goldcount'] = 0
        request.session['activities'] = []
    return render(request,'ninjagold/index.html')

def process(request,desto):
    if desto == "farm":
        earnings = random.randrange(10,21)
        request.session['goldcount'] += earnings
        new_activity = {
            'color' : 'green',
            'activity' : "Earned " + str(earnings) + " gold from the farm ("+str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) +")"
        }
    elif desto == "cave":
        earnings = random.randrange(5,11)
        request.session['goldcount'] += earnings
        new_activity = {
            'color' : 'green',
            'activity' : "Earned " + str(earnings) + " gold from the cave ("+str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) +")"
        }
    elif desto == "house":
        earnings = random.randrange(2,6)
        request.session['goldcount'] += earnings
        new_activity = {
            'color' : 'green',
            'activity' : "Earned " + str(earnings) + " gold from the house ("+str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) +")"
        }
    elif desto == "casino":
        direction = random.randrange(0,2)
        earnings = random.randrange(0,51)
        if direction == 0:
            request.session['goldcount'] -= earnings
            new_activity = {
                'color' : 'red',
                'activity' : "Entered a casino and lost " + str(earnings) + " gold... Ouch ... ("+str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) +")"
            }
        else:
            request.session['goldcount'] += earnings
            new_activity = {
                'color' : 'green',
                'activity' : "Entered a casino and won " + str(earnings) + " gold... Yay!!! ("+str(datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")) +")"
            }
    else:
        pass

    print
    request.session['activities'].insert(0,new_activity)
    print request.session['activities']
    return render(request, 'ninjagold/index.html')

def reset(request):
    # del request.session['activities']
    request.session['goldcount'] = 0
    request.session['activities'] = []
    return render(request, 'ninjagold/index.html')
