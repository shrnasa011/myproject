from django.conf.urls import url, include
#from django.conf.urls.defaults import *
from django.contrib import admin, auth
from login import views

app_name = 'login'

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^login/$', views.login, name="login"),
    #url(r''  , views.hey, name="hey"),
]
