from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile-picture/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    udemy = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class CategoryModel(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'

    def __str__(self):
        return self.name

class PostModel(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)  # Slug alanı
    image = models.ImageField(upload_to='content_image', blank=True, null=True)
    author = models.ForeignKey('CustomUserModel', on_delete=models.CASCADE, related_name='posts')
    category = models.ManyToManyField('CategoryModel', related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'posts'
        verbose_name_plural = 'Gönderiler'
        verbose_name = 'Gönderi'

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.author.username

class ContactModel(models.Model):
    email = models.EmailField(max_length=60, blank=False, null=False)
    name_surname = models.CharField(max_length=50, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact'
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.email
