from django import forms
from .models import Category,Product,Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title','photo',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title','content','photo',)
