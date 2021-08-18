from django.shortcuts import render
from .models import Bboard, Bboard_categories

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BbForm


def index(request):
	bboard_writes = Bboard.objects.all()
	categories = Bboard_categories.objects.all()
	return render(request, 'bboard/bboard.html', {'bboard_writes': bboard_writes, 
		'categories': categories})


def sorting(request, categori_id):
	categories = Bboard_categories.objects.all()
	bboard_writes = Bboard.objects.filter(categories=categori_id)
	return render(request, 'bboard/bboard.html', {'bboard_writes': bboard_writes, 
		'categories': categories})


class BbCreateView(CreateView):
	template_name = 'bboard/bboard_create.html'
	form_class = BbForm
	success_url = reverse_lazy('bboard:index')

	def get_context_date(self, **kwargs):
		context = super().get_context_date(**kwargs)
		context['categories'] = Bboard_categories.objects.all()
		return context
