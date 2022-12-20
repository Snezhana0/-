from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .forms import  LoginForm, RegisterForm
from .models import *


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'Главная.html', {'user': request.user})




def game(request):
    return render(request,'Игры.html')

def test(request):
    return render(request,'test.html')

def shrek(request):
    return render(request, 'шрек.html')

def twin (request):
    return render(request, 'Твин Пикс.html')

def depeche (request):
    return render(request, 'Depeche Mode.html')

def bowie (request):
    return render(request, 'Дэвид Боуи.html')

def lana (request):
    return render(request, 'Lana.html')

def victorin(request):
    return render(request,'Мои-викторины.html')

def about(request):
    return render(request,'О-Нас.html')

def regist(request):
    return render(request,'Регистрация.html')

def vhod(request):
    return render(request,'Войти.html')

def faq(request):
    posts = Faq.objects.all()
    return render(request,'FAQ.html', {'posts': posts})


def contact(request):
    return render(request,'Контакты.html')

def ind(request):
    return render(request,'index.html')

def base(request):
    return render(request, 'base.html')

# страница входа
def loginPage(request):

    # инициализируем объект класса формы
    form = LoginForm()

    # обрабатываем случай отправки формы на этот адрес
    if request.method == 'POST':

        # заполянем объект данными, полученными из запроса
        form = LoginForm(request.POST)

        # проверяем валидность формы
        if form.is_valid():
            # пытаемся авторизовать пользователя
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # если существует пользователь с таким именем и паролем,
                # то сохраняем авторизацию и делаем редирект
                login(request, user)
                return redirect('home')
            else:
                # иначе возвращаем ошибку
                form.add_error(None, 'Неверные данные!')

    # рендерим шаблон и передаем туда объект формы
    return render(request, 'login.html', {'form': form})

# регистрация
def registerPage(request):

    # инициализируем объект формы
    form = RegisterForm()

    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')
    # ренедерим шаблон и передаем объект формы
    return render(request, 'registration.html', {'form': form})




# выход
def doLogout(request):
    # вызываем функцию django.contrib.auth.logout и делаем редирект на страницу входа
    logout(request)
    return redirect('login')













