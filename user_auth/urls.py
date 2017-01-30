from django.conf.urls import url
from user_auth.forms import LoginForm
from . import views

urlpatterns = [
    url(r'/login', views.login_user, {'template_name' : 'login.html', 'authentication_form': LoginForm}, name="login"),
]