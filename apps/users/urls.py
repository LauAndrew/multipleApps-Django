from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^register$', views.index),
    url(r'^login$', views.login),
    url(r'^new$', views.index),
    url(r'^$', views.new),
]