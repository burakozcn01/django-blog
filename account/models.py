from django.db import models
from django.contrib.auth.models import AbstractUser


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