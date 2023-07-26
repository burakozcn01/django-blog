from django.contrib import admin
from .models import CategoryModel, PostModel, CommentModel, ContactModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'update_date', 'author']
    search_fields = ('title', 'content')

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_date', 'update_date')
    search_fields = ('author__username', 'content')

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name_surname', 'created_date')
    search_fields = ('email', 'name_surname')
