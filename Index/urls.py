from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('the-head-turners',views.auditorium,name='auditorium'),
    path('global-summit',views.global_summit,name='global_summit'),
    path('general-listing',views.general_listing,name='general_listing'),
    path('empaneled-vendor',views.empaneled_vendor,name='empaneled_vendor'),
    path('about-us',views.about,name='about'),
    path('membership',views.membership,name='membership'),
    path('members',views.members,name='members'),
    path('india-international-knit-fair',views.knit_event,name='knit_event'),
    path('glocal-manoeuvre-series-powerplay1',views.powerplay1_event,name='powerplay1_event'),
    path('glocal-manoeuvre-series-powerplay2',views.powerplay2_event,name='powerplay2_event'),
    path('award',views.award,name='award'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),


]
