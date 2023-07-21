from django.contrib import admin
from .models import categoryModel, contentModel, commentModel, contactModel


@admin.register(categoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(contentModel)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'update_date', 'author']
    search_fields = ('title', 'content')

@admin.register(commentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_date', 'update_date')
    search_fields = ('author__username', 'content')

@admin.register(contactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name_surname', 'created_date')
    search_fields = ('email', 'name_surname')
