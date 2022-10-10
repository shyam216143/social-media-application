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


#
# class Posts(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     comment_count = models.IntegerField(default=0)
#     content = models.TextField(max_length=4096, blank=True, null=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     is_type_share = models.BooleanField(default=False)  # This field type is a guess.
#     like_count = models.IntegerField(default=0)
#     post_photo = models.ImageField(upload_to='image', blank=True, null=True)
#     share_count = models.IntegerField(default=0)
#     author = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
#     shared_post = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)


# class Tags(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     date_created = models.DateTimeField(auto_created=True)
#     date_last_modified = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=64)
#     tag_use_counter = models.IntegerField(default=0)
#
#     class Meta:
#         managed = False
#         db_table = 'tags'
#
