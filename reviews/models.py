from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    photo = models.CharField(max_length=255)
    data_id = models.IntegerField()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    photo = models.CharField(max_length=255)
    review_product_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=50)
    content = models.TextField()
    review_photo = models.ImageField(blank=True, null=True, upload_to='review_images/')
    score = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')