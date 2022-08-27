from django.urls import path
from . views import *
urlpatterns=[
    path('',home),
    path('signup',signup,name = 'signup'),
    path('signin',signin,name = 'signin'),
    path('signout',signout,name = 'signout'),
    path('settings',settings,name = 'settings'),
    path('example',example,name = 'example'),
    path('upload',upload_post,name = 'upload_post')
]