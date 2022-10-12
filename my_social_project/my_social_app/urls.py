from django.urls import path

from .Views.ProfilePhotoView import UserProfilePhotoView

from .Views.ForgotPasswordView import SendPasswordResetEmailView
from .Views.PasswordResetThroughEmail import UserPasswordResetView

from .Views.ChangepasswordView import UserChangePasswordView

from .Views.LoginView import UserLoginView
from .Views.ProfiledataView import ProfileDataView

from .Views.RegisterView import UserRegistration
from .Views.UpdateInfoView import UpdateInfoView
from .Views.UserProfile import UserProfileView
from .Views.ChangeEmailView import ChangeEmailView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update/', UpdateInfoView.as_view(), name='update'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:id>/', ProfileDataView.as_view(), name='profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('change-email/', ChangeEmailView.as_view(), name='change-email'),
    path('forgot_password_send_email/', SendPasswordResetEmailView.as_view(), name='forgot_password_send_email'),
    path('reset-password/<str:uid>/<str:token>/', UserPasswordResetView.as_view(), name='forgot_password_send_email'),
    path('update/profile-photo/<int:id>/',UserProfilePhotoView.as_view(),name="profile-photo")

]
