from django.urls import path

from .Views.LoginView import UserLoginView

from .Views.RegisterView import UserRegistration
from .Views.UpdateInfoView import UpdateInfoView
from .Views.UserProfile import UserProfileView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update/', UpdateInfoView.as_view(), name='update'),
    path('profile/', UserProfileView.as_view(), name='profile'),

]
