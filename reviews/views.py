from django.shortcuts import render, redirect

# Create your views here.
def index_redirect(request):
    return redirect('reviews:index')

def index(request):
    return render(request, 'reviews/index.html')

def category(request):
    return render(request, 'reviews/category.html')

