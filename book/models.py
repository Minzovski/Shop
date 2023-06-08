from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=None)
    writer = models.CharField(max_length=50, default=None)
    pages = models.IntegerField(default=None)
    description = models.TextField(max_length=200, default=None)
    created = models.DateTimeField(auto_now_add=True, null=True)
    edited=models.DateTimeField(auto_now=True)
    published=models.DateTimeField(default=timezone.now)
    photo=models.ImageField(upload_to='book', blank=True)
    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name