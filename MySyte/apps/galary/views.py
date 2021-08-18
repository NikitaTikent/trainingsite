from django.shortcuts import render
from .models import Galary, Galary_fasttest
from .forms import GalaryForms

def index(request):
	forms = GalaryForms
	results = Galary.objects.all()
	result_test = Galary_fasttest.objects.filter(kind='c')
	return render(request, 'galary/galary.html', {'results': results, 'forms': forms, 'result_test': result_test})

def add(request):
	forms = GalaryForms
	results = Galary.objects.all()
	
	autor = request.POST['autor']
	photo_url = request.POST['photo_url']
	for_save = Galary(autor=autor, photo_url=photo_url)
	for_save.save()
	return render(request, 'galary/galary.html', {'results': results, 'forms': forms})
