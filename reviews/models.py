from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20)

class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='product_images/')

class Review(models.Model):
    title = models.CharField(max_length=20)
    score = models.IntegerField()
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='review_images/')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    created_at = models.DateTimeField(auto_now_add=True)