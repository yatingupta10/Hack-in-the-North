from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact.html$', views.contact, name='contact'),
    url(r'^about.html$', views.about, name='about'),
<<<<<<< HEAD
    url(r'^rate.html$', views.rate, name='rate'),
    url(r'^post/new/$', views.post_new, name='post_new'),

=======
    url(r'^rank$',views.rank,name='rank'),
    url(r'^rate.html$', views.about, name='rate'),
>>>>>>> 68341b327cca6029ed5cf81fa07c3283a5fd29b2
]