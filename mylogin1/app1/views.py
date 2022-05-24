from django.shortcuts import render
from django.http import HttpResponse  # added
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt   
import random



# Create your views here.
#it has to be a post to login, I guess, can't be a get
@csrf_exempt
def loginn(request):  # function added
    msg = ""
    if request.method == "POST":
        msg="POST"
        uname =signupuser(request)
        msg = msg + "  ... and user " + uname + "has been created"
        return HttpResponse(msg)
    else:
        msg = "GET"
        form = """
        <html>
        <body>
        <form method=post>
		<input type="submit" value="Submit the form">
		</form> 
		</body>
		</html>
		"""
        #return render (request, 'login.html')
        return HttpResponse(form)
		#return render (request, 'folio/home.html', {'projects':projects}) 

@csrf_exempt
def signupuser(request):
    i=random.randint(1, 99)
    uname = "mike"+str(i)
    user = User.objects.create_user(uname)
    user.save()
    login (request, user)
    return uname

@login_required
@csrf_exempt
def foo1(request):
    return HttpResponse ("you have to be logged in to see this")

@csrf_exempt
def foo2(request):
    return HttpResponse ("anyone can see this")


@login_required
def logoutt(request):
    logout(request)
    return HttpResponse("you are logged out")