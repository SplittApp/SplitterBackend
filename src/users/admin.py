from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Detail, Profile, Friend

admin.site.register(Detail)
admin.site.register(Profile)
admin.site.register(Friend)
