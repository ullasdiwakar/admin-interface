from django.conf.urls import url
from . import views
from forms import LoginForm

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login_user, {'template_name' : 'login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^home$', views.home, name='home'),
]