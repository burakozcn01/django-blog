from django.db import models
from autoslug import AutoSlugField 
from blog.models import categoryModel
from django.contrib.auth.models import User

class commentModel(models.Model):
    image = models.ImageField(upload_to='comment_image', blank=True, null=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(populete_from = 'title',unique=True)
    category = models.ManyToManyField('categoryModel',related_name='content', on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='contents', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Gönderiler'
        verbose_name = 'Gönderi'
        db_name = 'content'