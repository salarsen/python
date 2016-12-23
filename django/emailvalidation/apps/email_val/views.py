from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email

# Create your views here.
def index(request):
    return render(request, 'email_val/index.html')

def add_email(request):
    if request.method == "POST":
        response = Email.objects.validate_email(email_address=request.POST['email_address'])
        if response[0]:
            context = {
                'new_address':response[1],
                'email_addresses':Email.objects.all().order_by('-created_at'),
            }
            return render(request, 'email_val/success.html',context)
        else:
            messages.error(request, response[1])
            return redirect('/')
