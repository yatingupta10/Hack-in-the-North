from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^rate.html$', views.rate, name='rate'),
    url(r'^post/new/$', views.post_new, name='post_new'),

]