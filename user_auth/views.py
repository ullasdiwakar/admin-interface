from django.shortcuts import render
from django.contrib.auth import views as auth_views
from user_auth.forms import LoginForm

def login_user(request, template_name='login.html', authentication_form=LoginForm):
    if request.POST.has_key('remember_me'):
        request.session.set_expiry(1209600)
    return auth_views.login(request, template_name, authentication_form)
