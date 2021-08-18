from django.shortcuts import render
from .models import User, Cars, Details
from .forms import BankForm


def index(request):
	users = User.objects.all()
	cars = Cars.objects.all()
	return render(request, 'bank/bank.html', {'users': users, 'cars': cars})


def user_cards(request, user_id):
	users = User.objects.all()

	user = User.objects.get(id=user_id)
	user_cards = user.cards_number.all()

	context = {
		'users': users,
		'user_cards': user_cards,
		'form': BankForm
	}

	return render(request, 'bank/bank.html', context)


def car_details(request, car_id):
	details = Cars.objects.get(id=car_id).details.all()
	cars = Cars.objects.all()
	return render(request, 'bank/bank.html', {'details': details, 'cars': cars})


