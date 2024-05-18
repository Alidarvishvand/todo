from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    models = User 
    list_display = ("email", "is_active", "is_superuser")
    search_fields = ("email", "is_active", "is_superuser")
    ordering = ("email",)
    fieldsets=(
        ("authentication", {
        'fields': ('email','password'),
        }),
        ("permissions", {
        'fields': ('is_active','is_superuser','is_staff'),      
        }),
         ("group permissions", {
        'fields': ("groups","user_permissions"),
        }),
        ("important date", {
        'fields': ("last_login",),
        }),
)
     
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_active','is_staff', 'password1', 'password2'),
        }),
    )

admin.site.register(Profile)
admin.site.register(User,CustomUserAdmin)