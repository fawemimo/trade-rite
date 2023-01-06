from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



class ProfileAdmin(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [ProfileAdmin]
    list_display =('name','email','username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'name')
    readonly_fields = ('last_login', 'date_joined')
    search_fields = ('name','email')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_per_page = 25
    list_filter = ('date_joined','last_login','is_active')
    fieldsets = ()
    
   

