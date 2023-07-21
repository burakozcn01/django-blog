from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_active', 'date_joined', 'last_login')
    fieldsets = UserAdmin.fieldsets + ( (None, {'fields': ('profile_picture', 'linkedin', 'twitter', 'instagram', 'github', 'website', 'bio', 'udemy')}), )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')
    
admin.site.register(CustomUserModel, CustomAdmin)
