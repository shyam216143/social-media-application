from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .Views.VerifyEmailView import VerifyEmailView

from .Views.GetChatMessagesListView import GetChatMessagesList

# from .Views.ExistingPostDeleteView import ExistingPostDelete
from post_app.Views.ExistingPostDeleteView import ExistingPostDelete
# from .Views.ExistingPostShareDelete import ExistingPostShareDelete
from post_app.Views.ExistingPostShareDelete import ExistingPostShareDelete
# from .Views.ExistingPostUpdate import ExistingPostUpdate
from post_app.Views.ExistingPostUpdate import ExistingPostUpdate
# from .Views.GetFollowersDataView import GetFollowersData
from user_credential.Views.GetFollowersDataView import GetFollowersData
# from .Views.GetNotificationList import GetNotification
from notification_app.Views.GetNotificationList import GetNotification
# from .Views.GetPostByTagName import GetPostsBytagView
from post_app.Views.GetPostByTagName import GetPostsBytagView
# from .Views.GetPostCommentView import GetPostCommentView
from post_comment_app.Views.GetPostCommentView import GetPostCommentView
# from .Views.GetPostsByIdView import GetPostsByIdView
from post_app.Views.GetPostsByIdView import GetPostsByIdView

# from .Views.GetTagsView import GetTagsView
from tag_app.Views.GetTagsView import GetTagsView
# from .Views.GetUserPostsView import GetUserPostsview
from post_app.Views.GetUserPostsView import GetUserPostsview
from .Views.NotificationMarkAllReadView import NotificationMarkAllReadView
# from .Views.NotificationMarkAllSeenView import NotificationMarkAllSeenView
from notification_app.Views.NotificationMarkAllSeenView import NotificationMarkAllSeenView
# from .Views.PostCommentDeleteView import PostCommentDeleteView
from post_comment_app.Views.PostCommentDeleteView import PostCommentDeleteView
# from .Views.PostCommentLike import PostCommentLikeView
from post_comment_app.Views.PostCommentLike import PostCommentLikeView
# from .Views.PostCommentLikesListView import PostCommentLikesListView
from post_comment_app.Views.PostCommentLikesListView import PostCommentLikesListView
# from .Views.PostCommentUnikeView import PostCommentUnikeView
from post_comment_app.Views.PostCommentUnikeView import PostCommentUnikeView
# from .Views.PostCreateComment import PostCreateCommentView
from post_comment_app.Views.PostCreateComment import PostCreateCommentView
# from .Views.PostLikeView import PostLikeView
from post_app.Views.PostLikeView import PostLikeView
# from .Views.PostLikesListView import PostLikesListView
from post_app.Views.PostLikesListView import PostLikesListView
# from .Views.PostShareCreate import PostShareCreteView
from post_app.Views.PostShareCreate import PostShareCreteView
# from .Views.PostUnLikeView import PostUnlikeView
from post_app.Views.PostUnLikeView import PostUnlikeView
# from .Views.UserSearchView import UserSearchView
from search_app.Views.UserSearchView import UserSearchView

# from .Views.GetTimelinePosts import GetTimelinePostsview
from post_app.Views.GetTimelinePosts import GetTimelinePostsview

# from .Views.CreatePostView import CreatePostView
from post_app.Views.CreatePostView import CreatePostView
# from .Views.PostPhotoDelete import UserPostDelete
from post_app.Views.PostPhotoDelete import UserPostDelete
# from .Views.UnfollowUserView import UnfollowUserView
from Follow_Unfollow_app.Views.UnfollowUserView import UnfollowUserView

# from .Views.CoverPhotoView import UserCoverPhotoView
from user_credential.Views.CoverPhotoView import UserCoverPhotoView
# from .Views.FollowUserView import FollowUserView
from Follow_Unfollow_app.Views.FollowUserView import FollowUserView
# from .Views.ProfilePhotoView import UserProfilePhotoView
from user_credential.Views.ProfilePhotoView import UserProfilePhotoView

# from .Views.ForgotPasswordView import SendPasswordResetEmailView
from user_credential.Views.ForgotPasswordView import SendPasswordResetEmailView
# from .Views.PasswordResetThroughEmail import UserPasswordResetView
from user_credential.Views.PasswordResetThroughEmail import UserPasswordResetView

# from .Views.ChangepasswordView import UserChangePasswordView
from user_credential.Views.ChangepasswordView import UserChangePasswordView

# from .Views.LoginView import UserLoginView
from user_credential.Views.LoginView import UserLoginView

# from .Views.ProfiledataView import ProfileDataView
from user_credential.Views.ProfiledataView import ProfileDataView

# from .Views.RegisterView import UserRegistration
from user_credential.Views.RegisterView import UserRegistration
# from .Views.UpdateInfoView import UpdateInfoView
from user_credential.Views.UpdateInfoView import UpdateInfoView
# from .Views.UserFollowerList import UserFollowerListView
from Follow_Unfollow_app.Views.UserFollowerList import UserFollowerListView
# from .Views.UserFollowingList import UserFollowingListView
from Follow_Unfollow_app.Views.UserFollowingList import UserFollowingListView
from .Views.UserProfile import UserProfileView
# from .Views.ChangeEmailView import ChangeEmailView
from user_credential.Views.ChangeEmailView import ChangeEmailView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register_in_user_credential'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update/', UpdateInfoView.as_view(), name='update'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:id>/', ProfileDataView.as_view(), name='profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('change-email/', ChangeEmailView.as_view(), name='change-email'),
    path('forgot_password_send_email/', SendPasswordResetEmailView.as_view(), name='forgot_password_send_email'),
    path('reset-password/<str:uid>/<str:token>/', UserPasswordResetView.as_view(), name='forgot_password_send_email'),
    path('verify-email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='forgot_password_send_email'),
    path('update/profile-photo/',UserProfilePhotoView.as_view(),name="profile-photo"),
    path('update/cover-photo/', UserCoverPhotoView.as_view(), name="profile-photo"),
    path('follow-user/', FollowUserView.as_view(), name="follow-user"),
    path('unfollow-user/', UnfollowUserView.as_view(), name="unfollow-user"),
    path('user/following/<int:id>/', UserFollowingListView.as_view(), name="follow-user"),
    path('user/follower/<int:id>/', UserFollowerListView.as_view(), name="follow-user"),
    path('user/createpost/', CreatePostView.as_view(), name="follow-user"),
    path('user1/', GetTimelinePostsview.as_view(), name="get-user-posts"),
    path('tags/', GetTagsView.as_view(), name="get-used-tags"),
    path('users/posts/', GetUserPostsview.as_view(), name="get-user-posts"),
    path('posts/<int:id>/', GetPostsByIdView.as_view(), name="get-user-posts"),
    path('posts/tags/<str:name>/', GetPostsBytagView.as_view(), name="get-user-posts"),
    path('users/search/', UserSearchView.as_view(), name="get-user-posts"),
    path('posts/<int:post_id>/photo/delete/', UserPostDelete.as_view(), name="get-user-posts"),
    path('posts/<int:post_id>/update/', ExistingPostUpdate.as_view(), name="get-post_update"),
    path('posts/<int:post_id>/delete/', ExistingPostDelete.as_view(), name="get-post_delete"),
    path('posts/<int:post_id>/share/delete/', ExistingPostShareDelete.as_view(), name="get-post_delete"),
    path('posts/<int:post_id>/like/', PostLikeView.as_view(), name="post_like"),
    path('posts/<int:post_id>/likes/', PostLikesListView.as_view(), name="post_like"),
    path('posts/<int:post_id>/unlike/', PostUnlikeView.as_view(), name="post_like"),
    path('posts/<int:post_id>/comments/create/', PostCreateCommentView.as_view(), name="post_like"),
    path('posts/<int:post_id>/comments/', GetPostCommentView.as_view(), name="get_post_comment"),
    path('posts/comments/<int:commentId>/like/', PostCommentLikeView.as_view(), name="post_comment_like"),
    path('posts/comments/<int:commentId>/unlike/', PostCommentUnikeView.as_view(), name="post_comment_unlike"),
    path('posts/comments/<int:commentId>/likes/', PostCommentLikesListView.as_view(), name="post_comment_likes_list"),
    path('posts/<int:post_id>/comments/<int:commentId>/delete/', PostCommentDeleteView.as_view(), name="post_comment_likes_list"),
    path('posts/<int:post_id>/share/create/', PostShareCreteView.as_view(), name="post_comment_likes_list"),
    path('notifications/', GetNotification.as_view(), name="Notification_list"),
    path('notifications/mark-seen/', NotificationMarkAllSeenView.as_view(), name="Notification_set_all_seen_True"),
    path('notifications/mark-read/', NotificationMarkAllReadView.as_view(), name="Notification_set_all_read_True"),
    path('<int:user_id>/followers_data/', GetFollowersData.as_view(), name="Notification_set_all_read_True"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('chat_data/current_user/', GetChatMessagesList.as_view(), name='token_refresh'),

]
