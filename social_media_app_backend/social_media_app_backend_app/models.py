from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager



class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,

        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        if extra_fields.get('is_admin') is not True:
            raise ValueError('super user must have is_staff true')

        user.save(using=self._db)
        return user




class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name="Email Address", unique=True)
    account_verified = models.TextField(blank=True, null=True)  # This field type is a guess.
    birth_date = models.DateTimeField(blank=True, null=True)
    cover_photo = models.CharField(max_length=256, blank=True, null=True)
    current_city = models.CharField(max_length=128, blank=True, null=True)
    date_last_modified = models.DateTimeField(blank=True, null=True)
    edu_institution = models.CharField(max_length=128, blank=True, null=True)
    email_verified = models.TextField(blank=True, null=True)  # This field type is a guess.
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    first_name = models.CharField(max_length=64)
    follower_count = models.IntegerField(blank=True, null=True)
    following_count = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    hometown = models.CharField(max_length=128, blank=True, null=True)
    intro = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    profile_photo = models.CharField(max_length=256, blank=True, null=True)
    role = models.CharField(max_length=32)
    workplace = models.CharField(max_length=128, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = None
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    calling_code = models.CharField(max_length=4, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_last_modified = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'countries'
