from django.db import models
from account.models import CustomUserModel
from blog.models.abstract_models import DateAbstractModel

class contactModel(DateAbstractModel):
    email = models.EmailField(max_length=60, blank=False, null=False)
    name_surname = models.CharField(max_length=50, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'contact'
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.email