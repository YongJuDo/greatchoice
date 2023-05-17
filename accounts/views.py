from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm , CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount
from django.core.files import File
import urllib.request
from django.core.paginator import Paginator

def kakao_disconnect(request):
    if request.user.is_authenticated:
        # 사용자의 카카오 소셜 계정 연결 끊기
        SocialAccount.objects.filter(user=request.user, provider='kakao').delete() 
        # auth_logout(request)
    # 계정 삭제 후 리다이렉트할 URL
        redirect_url = 'reviews:index'
    return redirect('reviews:index')


def basic_login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def basic_logout(request):
    auth_logout(request)
    return redirect('reviews:index')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('reviews:index')


def basic_signup(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if not user.profile_image:
                image_url = 'https://picsum.photos/200'
                response = urllib.request.urlopen(image_url)
                user.profile_image.save('default_image.jpg', File(response), save=True)
            user.save()
            auth_login(request, user)
            return redirect('reviews:index') 
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('reviews:index') 
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def update(request):
    User = get_user_model()
    person = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:profile', user.username) 
    else:
        form = CustomUserChangeForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('reviews:index')


@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)    
    return redirect('accounts:profile', person.username)


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    is_kakao_connected = SocialAccount.objects.filter(user=request.user, provider='kakao').exists()
    reviews = person.review_set.all()
    review_count = len(reviews)
    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 4)  # 한 페이지에 4개씩 표시하도록 수정
    page_obj = paginator.get_page(page)
    context = {
        'is_kakao_connected': is_kakao_connected,
        'person': person,
        'review_count': review_count,
        'reviews': page_obj,
    }
    return render(request, 'accounts/profile.html', context)


def set_default_profile_image(request):
    user = request.user
    # 이미지 URL에서 이미지를 가져와서 프로필 이미지로 설정
    image_url = 'https://picsum.photos/200'
    response = urllib.request.urlopen(image_url)
    user.profile_image.save('default_image.jpg', File(response), save=True)

    return redirect('accounts:profile', request.user.username)