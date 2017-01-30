from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

@login_required(login_url = "user_auth/login/")
def home(request):
    return render(request,"home.html")


