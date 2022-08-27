from django.contrib import admin
from .models import profile, posting, likepost
# Register your models here.
admin.site.register(profile)
admin.site.register(posting)
admin.site.register(likepost)