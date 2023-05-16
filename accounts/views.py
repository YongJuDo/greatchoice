from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm , CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount
from django.views import View
from .models import CustomUser

# Create your views here.
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
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('reviews:profile') 
    else:
        form = CustomUserChangeForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def basic_signup(request):
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
def logout(request):
    auth_logout(request)
    return redirect('reviews:index')

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
    user = request.user
    User = get_user_model()
    person = User.objects.get(username=username)
    is_kakao_connected = SocialAccount.objects.filter(user=request.user, provider='kakao').exists()
    context = {
        'is_kakao_connected': is_kakao_connected,
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

