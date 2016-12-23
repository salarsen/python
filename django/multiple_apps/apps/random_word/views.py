from django.shortcuts import render
import random
import string
# Create your views here.

def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    # else:
    #     request.session['attempt'] += 1
    context = {
        'random_word':random_generator()
    }
    return render(request, 'random_word/index.html',context)

def new_word(request):
    request.session['attempt'] += 1
    # context = {
    #     'random_word':random_generator()
    # }
    # return render(request, 'random_word/index.html',context)
    return index(request)

def random_generator(size=14, chars=string.ascii_uppercase + string.digits): #string size 14 characters, chars composed of uppercase characters and digits in string form
    # print chars
    return ''.join(random.choice(chars) for x in range(size))
