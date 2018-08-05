from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.get_name, name='get_name'),

   ]