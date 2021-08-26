from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from .models import test


def index(request):
	test_objects = test.objects.all()

	context = {
		'test_objects': test_objects,
	}
	return render(request, 'classview/classview.html', context)


class NameClassView(DetailView):
	model = test

