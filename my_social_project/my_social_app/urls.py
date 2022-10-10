from django.urls import path

from my_social_app.Views.LoginView import UserLoginView

from .Views.RegisterView import UserRegistration


urlpatterns = [
    path('register/',UserRegistration.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
   
]

