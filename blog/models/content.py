from django.db import models
from autoslug import AutoSlugField 
from blog.models import categoryModel
from ckeditor.fields import RichTextField
from account.models import CustomUserModel

class contentModel(models.Model):
    image = models.ImageField(upload_to='content_image', blank=True, null=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    category = models.ManyToManyField('categoryModel',related_name='content')
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='contents')

    class Meta:
        verbose_name_plural = 'Gönderiler'
        verbose_name = 'Gönderi'
        db_table = 'content'

    def __str__(self):
         return self.title