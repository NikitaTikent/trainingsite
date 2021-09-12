from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.paginator import Paginator
from django.db.models import Count
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME

from .models import Galary, Galary_fasttest
from .forms import GalaryForms, Galary_detail

from aunthenticated.decorators import aunthenticated_user
import math


test_form = modelformset_factory(model=Galary,
	fields=('autor', 'photo_url'),
	can_order=True,
	can_delete=True)



def index(request):
	forms = GalaryForms
	results = Galary.objects.all()
	
	paginator = Paginator(results, 2)

	if 'page' in request.GET:
		page_num = request.GET['page']
	else:
		page_num = 1

	page = paginator.get_page(page_num)
	
	count_writes = Galary.objects.aggregate(count=Count('autor'))
	last_page = count_writes['count']/2
	last_page = math.ceil(last_page)

	context = {
	'results': page.object_list, 
	'forms': forms, 
	'page': page, 
	'last_page': last_page}
	
	return render(request, 'galary/galary.html', context)


@aunthenticated_user
def add(request):
	if request.method == 'POST':
		formset = test_form(request.POST)
		if formset.is_valid():
			for form in formset:
				if form.cleaned_data:
					galary_write = form.save(commit=False)

					if form.cleaned_data[ORDERING_FIELD_NAME]:
						galary_write.order = form.cleaned_data[ORDERING_FIELD_NAME]
					else:
						galary_write.order = 1
					
					if form.cleaned_data['DELETE']:
						galary_write.delete()
					else:
						galary_write.save()

			return redirect('galary:add')
		else:
			context = {
				'form': test_form
			}
			return render(request, 'galary/galary_info.html', context)
	else:
		context = {
			'form': test_form
		}
		return render(request, 'galary/galary_info.html', context)


class Galary_info(FormView):
	template_name = 'galary/galary_info.html'
	form_class = Galary_detail
	initial = {}
	success_url = '/galary'

	def get_form_kwargs(self):
		self.data = super().get_form_kwargs()
		return self.data

	def form_valid(self, form):
		autor_valid = self.data['data']['age']
		if int(autor_valid) == 5:
			form.save()
			return super().form_valid(form)
		else:
			return redirect('galary:test')

	def get_form(self, form_class=None):
		self.object = super().get_form(form_class)
		return self.object


class Calary_update(UpdateView):
	model = Galary
	models_form = GalaryForms
	fields = ('autor', 'photo_url')
	template_name = 'galary/galary_info.html'


class Galary_delete(DeleteView):
	model = Galary
	template_name = 'galary/galary_delete.html'
	success_url = '/galary'
