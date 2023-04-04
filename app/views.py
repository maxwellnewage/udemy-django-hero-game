from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from app.forms import UserLoginForm, UserRegisterForm

from blog.models import Post
from character.models import Player


def index(request):
    cat = request.GET.get('cat')
    best_players = Player.objects.order_by('-score')[:5]
    recent_players = Player.objects.order_by('-created')[:5]

    if cat is None:
        posts = Post.objects.all()[:3]
    else:
        posts = Post.objects.filter(category__icontains=cat)[:3]

    return render(request, 'index.html', {
        'posts': posts,
        'best_players': best_players,
        'recent_players': recent_players
    })


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserLoginForm()

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectas!')

    return render(request, 'login_register.html', {
        'page': 'login',
        'form': form,
        'submit_value': 'Ingresar'
    })


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ocurrió un error durante el registro!')

    return render(request, 'login_register.html', {
        'page': 'register',
        'form': form,
        'submit_value': 'Registrarse'
    })


def user_logout(request):
    logout(request)
    return redirect('home')
