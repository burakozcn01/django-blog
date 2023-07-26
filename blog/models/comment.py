from django.db import models
from blog.models import PostModel
from account.models import CustomUserModel
from blog.models.abstract_models import DateAbstractModel

class CommentModel(DateAbstractModel):
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comments')
    content = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(blank=False, null=False)


    class Meta:
        db_table = 'comment'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.author.username