from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^about.html$', views.contact, name='about'),
]