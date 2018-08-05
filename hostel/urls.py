from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', login, {'template_name': 'hostel/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'hostel/logout.html'}),
]