from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle")
    content = RichTextField(verbose_name="Content", blank=True, default='')
    image = models.ImageField(verbose_name="Image", upload_to="services", blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
