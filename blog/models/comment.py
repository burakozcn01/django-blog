from django.db import models
from django.contrib.auth.models import User
from blog.models import contentModel

class commentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    content = models.ForeignKey(contentModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'comment'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.author.username