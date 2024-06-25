from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel, CategoryModel, PostModel, CommentModel, ContactModel

@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', 'linkedin', 'twitter', 'instagram', 'github', 'website', 'bio', 'udemy')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar', 'linkedin', 'twitter', 'instagram', 'github', 'website', 'bio', 'udemy')}),
    )

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'update_date', 'author']
    search_fields = ('title', 'content')

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_date', 'update_date')
    search_fields = ('author__username', 'post__title')

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name_surname', 'created_date')
    search_fields = ('email', 'name_surname')
