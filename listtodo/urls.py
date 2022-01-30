from django.conf.urls import url
from . import views

app_name = 'globivacppapp'

urlpatterns = [
    url(r'^signin/$', views.signin),
    url(r'^signup/$', views.signup),
    url(r'^home/$', views.home),
    url(r'^tweet/$', views.dotweet),
    url(r'^follow/$', views.dofollow),
    ]

