from django.contrib import admin
from .models import categoryModel, contentModel, commentModel, contactModel

admin.site.register(categoryModel)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'change_date', 'author')
    search_fields = ('title', 'content')

admin.site.register(contentModel, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_date', 'update_date')
    search_fields = ('author__username', 'content')

admin.site.register(commentModel, CommentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name_surname', 'created_date')
    search_fields = ('email', 'name_surname')

admin.site.register(contactModel, ContactAdmin)