from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(unique=True, populate_from = 'name')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'