from django.contrib import admin
from .models import categoryModel, commentModel

admin.site.register(categoryModel)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'change_date', 'author')
    search_fields = ('title', 'content')

admin.site.register(commentModel, PostAdmin)
