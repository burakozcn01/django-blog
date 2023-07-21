from  django.db import models
from autoslug import AutoSlugField

class categoryModel(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'

    def __str__(self):
        return self.name