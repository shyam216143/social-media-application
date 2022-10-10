from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .model1 import Countries,Tags

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        ('user Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'username', 'first_name', 'last_name', 'cover_photo','profile_photo', 'current_city', 'edu_institution',
            'follower_count', 'following_count', 'gender', 'hometown', 'intro', 'workplace', 'country')}),
        ('Permissions', {'fields': (
            'is_admin', 'is_staff', 'is_superuser', 'is_active', 'role', 'account_verified', 'email_verified',
            'enabled')}),
        ('Important Dates', {'fields': ('date_last_modified','join_date','updated_at','created_at')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('id', 'email')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.

admin.site.register(Countries)
admin.site.register(Tags)
