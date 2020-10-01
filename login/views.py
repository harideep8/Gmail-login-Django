from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def welcome(request):
    user=request.user
    context={'user', user}
    return render(request,'login/welcome.html',context=context)
