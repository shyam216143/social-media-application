from django.urls import path

from my_social_app.Views.GetTagsView import GetTagsView

from .Views.GetTimelinePosts import GetTimelinePostsview

from .Views.CreatePostView import CreatePostView
from .Views.UnfollowUserView import UnfollowUserView

from .Views.CoverPhotoView import UserCoverPhotoView
from .Views.FollowUserView import FollowUserView
from .Views.ProfilePhotoView import UserProfilePhotoView

from .Views.ForgotPasswordView import SendPasswordResetEmailView
from .Views.PasswordResetThroughEmail import UserPasswordResetView

from .Views.ChangepasswordView import UserChangePasswordView

from .Views.LoginView import UserLoginView
from .Views.ProfiledataView import ProfileDataView

from .Views.RegisterView import UserRegistration
from .Views.UpdateInfoView import UpdateInfoView
from .Views.UserFollowerList import UserFollowerListView
from .Views.UserFollowingList import UserFollowingListView
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
    path('update/profile-photo/',UserProfilePhotoView.as_view(),name="profile-photo"),
    path('update/cover-photo/', UserCoverPhotoView.as_view(), name="profile-photo"),
    path('follow-user/', FollowUserView.as_view(), name="follow-user"),
    path('unfollow-user/', UnfollowUserView.as_view(), name="unfollow-user"),
    path('user/following/', UserFollowingListView.as_view(), name="follow-user"),
    path('user/follower/', UserFollowerListView.as_view(), name="follow-user"),
    path('user/createpost/', CreatePostView.as_view(), name="follow-user"),
    path('user1/', GetTimelinePostsview.as_view(), name="get-user-posts"),
    path('tags/', GetTagsView.as_view(), name="get-used-tags"),

]
