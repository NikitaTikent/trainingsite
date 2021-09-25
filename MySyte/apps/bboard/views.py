from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory


from .forms import BbForm, SearhForm, ImgForm
from .models import Bboard, Bboard_categories, Img


def index(request):
	bboard_writes = Bboard.objects.all()
	categories = Bboard_categories.objects.all()
	paginator = Paginator(bboard_writes, 2)
	if 'page' in request.GET:
		page_num = request.GET['page']
	else:
		page_num = 1

	page = paginator.get_page(page_num)

	return render(request, 'bboard/bboard.html', {'bboard_writes': page.object_list, 
		'categories': categories, 'page': page})


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


class Bboard_update(UpdateView):
	model = Bboard
	template_name = 'bboard/bboard_edit.html'
	models_form = BbForm
	fields = ('title', 'coast', 'description', 'categories')
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Bboard_categories.objects.all()
		return context


class Bboard_delete(DeleteView):
	model = Bboard
	success_url = '/'
	template_name = 'bboard/bboard_delete.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Bboard_categories.objects.all()
		return context


def bboard_and_categories(request, category_id):
	bbsc = inlineformset_factory(Bboard_categories, Bboard, form = BbForm, extra=1)
	category = Bboard_categories.objects.get(id=category_id)
	if request.method == 'POST':
		formset = bbsc(request.POST, instance=category)
		if formset.is_valid():
			formset.save()
			return redirect('bboard:index')
	else:
		form = bbsc(instance=category)
	context = {
		'form': form
	}
	return render(request, 'bboard/bboard_create.html', context)


def bboard_searh(request):
	if request.method == 'POST':
		form = SearhForm(request.POST)
		if form.is_valid():
			description = form.cleaned_data['description']
			category = form.cleaned_data['category'].pk
			searh_res = Bboard.objects.filter(description__icontains=description,
				categories=category)
			if len(searh_res) < 1:
				searh_res = 'None'
			context = {'result': searh_res}
		else:
			context = {'form': form}

		return render(request, 'bboard/searh_bboard.html', context)
	else:
		form = SearhForm()
		context = {'form': form}
		return render(request, 'bboard/searh_bboard.html', context)


def add_img(request):
	if request.method == 'POST':
		form = ImgForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('bboard:index')
		else:
			return render(request, 'bboard/add_img.html', {'forms': form})
	else:
		forms = ImgForm()
		images = Img.objects.all()

		context = {'forms': forms, 'images': images}
		return render(request, 'bboard/add_img.html', context)


def delete_img(request, img_pk):
	write = Img.objects.get(pk=img_pk)
	write.delete()
	return redirect('bboard:add_img')

