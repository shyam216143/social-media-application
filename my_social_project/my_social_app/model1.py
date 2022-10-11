from django.db import models
from django_countries.fields import CountryField


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = CountryField()




#
# class User(AbstractUser):
#     email = models.EmailField(unique=True, verbose_name="Email Address")
#     username = None
#     account_verified = models.TextField(blank=True, null=True)  # This field type is a guess.
#     birth_date = models.DateTimeField(blank=True, null=True)
#     cover_photo = models.ImageField(max_length=256, blank=True, null=True)
#     current_city = models.CharField(max_length=128, blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     edu_institution = models.CharField(max_length=128, blank=True, null=True)
#     email_verified = models.TextField(blank=True, null=True)  # This field type is a guess.
#     enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
#     follower_count = models.IntegerField(blank=True, null=True)
#     following_count = models.IntegerField(blank=True, null=True)
#     gender = models.CharField(max_length=16, blank=True, null=True)
#     hometown = models.CharField(max_length=128, blank=True, null=True)
#     intro = models.CharField(max_length=100, blank=True, null=True)
#     join_date = models.DateTimeField(blank=True, null=True)
#     profile_photo = models.CharField(max_length=256, blank=True, null=True)
#     role = models.CharField(max_length=32)
#     workplace = models.CharField(max_length=128, blank=True, null=True)
#     country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = MyUserManager()
#
#     def __str__(self):
#         return self.email
#
# class User(AbstractUser):
#     username = models.CharField(max_length=255, blank=True)
#     email = models.EmailField(unique=True, verbose_name="Email Address")
#     account_verified = models.BooleanField(default=False)  # This field type is a guess.
#     birth_date = models.DateTimeField(blank=True, null=True)
#     cover_photo = models.ImageField(upload_to='image', blank=True, null=True)
#     current_city = models.CharField(max_length=255, blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     edu_institution = models.CharField(max_length=128, blank=True, null=True)
#     email_verified = models.BooleanField(default=False)  # This field type is a guess.
#     enabled = models.BooleanField(default=False)  # This field type is a guess.
#     follower_count = models.IntegerField(default=0)
#     following_count = models.IntegerField(default=0)
#     gender = models.CharField(max_length=16, blank=True, choices=GENDER_CHOICES, default='1')
#     hometown = models.CharField(max_length=255, blank=True, null=True)
#     intro = models.TextField(max_length=300, blank=True, null=True)
#     join_date = models.DateTimeField(default=timezone.now)
#     profile_photo = models.ImageField(upload_to='image', blank=True, null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#     role = models.CharField(max_length=32)
#     workplace = models.CharField(max_length=128, blank=True, null=True)
#     country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

# class Tags(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     date_created = models.DateTimeField(auto_created=True)
#     date_last_modified = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=64)
#     tag_use_counter = models.IntegerField(default=0)

#     class Meta:
#         managed = False
#         db_table = 'tags'

# class Tags(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(unique=True, max_length=64)
#     tag_use_counter = models.IntegerField()
# #
#     class Meta:
#         managed = False
#         db_table = 'tags'
