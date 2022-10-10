from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .manager import MyUserManager
from .model1 import Countries

GENDER_CHOICES = (
    ('1', 'None'),
    ('2', 'Male'),
    ('3', 'Female'),
    ('4', 'Transgender'),

)


class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True, verbose_name="Email Address")
    account_verified = models.BooleanField(default=False)  # This field type is a guess.
    birth_date = models.DateTimeField(blank=True, null=True)
    cover_photo = models.ImageField(upload_to='image', blank=True, null=True)
    current_city = models.CharField(max_length=255, blank=True, null=True)
    date_last_modified = models.DateTimeField(default=timezone.now)
    edu_institution = models.CharField(max_length=128, blank=True, null=True)
    email_verified = models.BooleanField(default=False)  # This field type is a guess.
    enabled = models.BooleanField(default=False)  # This field type is a guess.
    follower_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    gender = models.CharField(max_length=16, blank=True, choices=GENDER_CHOICES, default='1')
    hometown = models.CharField(max_length=255, blank=True, null=True)
    intro = models.TextField(max_length=300, blank=True, null=True)
    join_date = models.DateTimeField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='image', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=32)
    workplace = models.CharField(max_length=128, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.email

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment_count = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=4096, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_last_modified = models.DateTimeField(blank=True, null=True)
    is_type_share = models.BooleanField(default=True)  # This field type is a guess.
    like_count = models.IntegerField(default=0,blank=True, null=True)
    post_photo = models.CharField(max_length=255, blank=True, null=True)
    share_count = models.IntegerField(default=0,blank=True, null=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    shared_post = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    def __str__(self) :
        return [self.content]



class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_last_modified = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=64)
    tag_use_counter = models.IntegerField(default=0)
    def __str__(self) :
        return [self.name]


class FollowUsers(models.Model):
    followed = models.ForeignKey('User', on_delete=models.CASCADE,related_name="Following")
    follower = models.ForeignKey('User', on_delete=models.CASCADE,related_name="Follower")

    def __str__(self) :
        return [self.followed + self.followers]





class PostLike(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    liker = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self) :
        return [self.post]


class PostTag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

  
    def __str__(self) :
      return [self.tag]

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=1024, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_last_modified = models.DateTimeField(blank=True, null=True)
    like_count = models.IntegerField(default=0,blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) :
      return [self.content]


class CommentLikes(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
      return [self.comment]


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_last_modified = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    is_read = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_seen = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.CharField(max_length=255)
    owning_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    owning_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='receiver')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='sender')

    def __str__(self) :
      return [self.id]