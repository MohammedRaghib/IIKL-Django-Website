from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_category')
    subcategory = models.ForeignKey('Sub_Category', on_delete=models.CASCADE, blank=True, null=True, related_name='product_sub_category')
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    image = CloudinaryField('image', null=True, blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return f'{self.name}'
