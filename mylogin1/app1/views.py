from django.shortcuts import render
from django.http import HttpResponse  # added
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.
#it has to be a post to login, I guess, can't be a get
def login(request):  # function added
    msg = ""
    if request.method == "POST":
        msg="POST"
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
        return HttpResponse (form)
        
