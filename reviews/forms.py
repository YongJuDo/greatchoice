from django import forms
from .models import Product, Review, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title','photo',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review_title','content','review_photo',)

    review_title = forms.CharField(
        label='제목',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': '제목',
            }
        )
    )

    content = forms.CharField(
        label='내용',
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': '내용',
            }
        )
    )


    review_photo = forms.ImageField(
        label='이미지',
        label_suffix='',
        required = False,
        widget=forms.FileInput (
            attrs={
                'placeholder': '이미지',
            }
        )
    )

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)