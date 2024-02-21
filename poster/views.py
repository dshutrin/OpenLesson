from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import *


# Create your views here.
def welcome(request):
	if request.user.is_anonymous:
		return HttpResponseRedirect('/login')
	else:
		HttpResponseRedirect('/home')


def login_view(request):
	form = LoginForm()
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		usr = authenticate(request, username=username, password=password)
		if usr is not None:
			login(request, usr)
			return HttpResponseRedirect('/home')
		else:
			form = LoginForm(request.POST)

	return render(request, 'auth/login.html', {'form': form, 'title': 'Авторизация'})


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login')


def register_view(request):
	form = RegForm()
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]
		usr = User.objects.create_user(username=username, password=password, email=email)
		usr.save()
		login(request, usr)
		return HttpResponseRedirect('/home')

	return render(request, 'auth/register.html', {'form': form, 'title': 'Регистрация'})


def home(request):


	return render(request, "poster/home.html", {'title': 'Главная'})
