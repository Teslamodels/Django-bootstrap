from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Create, Change, CustomUser

class Admin(UserAdmin):
    add_form = Create
    form = Change
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'password', 'BIO']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('BIO', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('BIO', )}),
    )

admin.site.register(CustomUser, Admin)