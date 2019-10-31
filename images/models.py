from django.db import models

# Create your models here.
class Photo(models.Model):
    image           = models.ImageField()
    desc            = models.TextField(max_length=255, blank=True)
    uploaded_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-uploaded_at',)
        verbose_name = 'Photo' 
        verbose_name_plural = 'Photos'