from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import LoginForm
from django.contrib.auth import views as auth_views

@login_required(login_url = "login/")
def home(request):
    return render(request,"home.html")

def login_user(request, template_name='login.html', authentication_form=LoginForm):
    if request.POST.has_key('remember_me'):    
        request.session.set_expiry(1209600)
    return auth_views.login(request, template_name, authentication_form)
