from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from models import Event, Announcements, UserProfile

class MyUserProfile(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','first_name','last_name')}
        ),
    )

admin.site.register(Event)
admin.site.register(Announcements)
admin.site.unregister(User)
admin.site.register(User, MyUserProfile)
admin.site.register(UserProfile)
