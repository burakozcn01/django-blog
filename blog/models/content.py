from django.db import models
from autoslug import AutoSlugField 
from blog.models import categoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class contentModel(models.Model):
    image = models.ImageField(upload_to='content_image', blank=True, null=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    category = models.ManyToManyField('categoryModel',related_name='content')
    author = models.ForeignKey(User,related_name='contents', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Gönderiler'
        verbose_name = 'Gönderi'
        db_table = 'content'

    def __str__(self):
         return self.title