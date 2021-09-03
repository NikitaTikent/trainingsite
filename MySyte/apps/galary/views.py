from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.edit import UpdateView

from .models import Galary, Galary_fasttest
from .forms import GalaryForms

from aunthenticated.decorators import aunthenticated_user



def index(request):
	forms = GalaryForms
	results = Galary.objects.all()
	result_test = Galary_fasttest.objects.filter(kind='c')
	return render(request, 'galary/galary.html', {'results': results, 'forms': forms, 
		'result_test': result_test})


@aunthenticated_user
def add(request):
	forms = GalaryForms
	results = Galary.objects.all()
	
	autor = request.POST['autor']
	photo_url = request.POST['photo_url']
	for_save = Galary(autor=autor, photo_url=photo_url)
	Galary.objects.update_or_create(photo_url=photo_url, defaults={'autor': autor})
	return render(request, 'galary/galary.html', {'results': results, 'forms': forms})


class Galary_info(FormView):
	template_name = 'galary/galary_info.html'
	form_class = GalaryForms
	initial = {'autor': '1'}

	@aunthenticated_user
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

	def get_form(self, form_class=None):
		self.object = super().get_form(form_class)
		return self.object

	def get_succes_url(self):
		return reverse('courses:index')


class Calary_update(UpdateView):
	model = Galary
	models_form = GalaryForms
	fields = ('autor', 'photo_url')
	template_name = 'galary/galary_info.html'
