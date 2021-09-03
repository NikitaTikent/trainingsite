from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unaunthenticated_user
from .forms import *


@unaunthenticated_user
def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/blog')
		else:
			messages.info(request, 'Некорректно')
	context = {}
	return render(request, 'login.html', context)


def logout_user(request):
	logout(request)
	return redirect('/blog')
