from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

def is_authenticated(user):
    return user.is_authenticated

is_authenticated.boolean = True 

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', is_authenticated)

admin.site.unregister(User)  
admin.site.register(User, CustomUserAdmin)  

