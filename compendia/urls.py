from django.conf.urls import url
from . import views

app_name = "compendia"

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
#    url(r'^signup/$', views.signup, name="signup"),
#    url(r'^logout/$', views.logout, name="logout"),
]
