from django.urls import path
from App_Login import views
from django.contrib.auth import views as auth_views

app_name = 'App_Login'

urlpatterns=[
    path('glocal-manoeuvre-series/',views.register,name='register'),
    # path('login/',views.login,name='login'),
    # path('logout/',views.logout,name='logout'),
    # path('payment/',views.payment,name='payment'),
    # path('handlerequest/', views.handlerequest, name = 'handlerequest'),




]