from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumb = models.ImageField(upload_to='category_thumbnails',blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    pic1 = models.ImageField(upload_to='category_thumbnails',blank=True, null=True)
    pic2 = models.ImageField(upload_to='category_thumbnails',blank=True, null=True)
    pic3 = models.ImageField(upload_to='category_thumbnails',blank=True, null=True)
    pic4 = models.ImageField(upload_to='category_thumbnails',blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name