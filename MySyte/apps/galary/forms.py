from django import forms
from .models import Galary

class GalaryForms(forms.ModelForm):
	class Meta:
		model = Galary
		fields = ('autor', 'photo_url')


class Galary_detail(forms.ModelForm):
	autor = forms.CharField(label='Имя автора')
	photo_url = forms.CharField(label='Сылка на фото')
	age = forms.IntegerField(label='Возраст')
	#publication_date = forms.DateField(label='Выберите дату публикации')

	class Meta:
		model = Galary
		fields = ('autor', 'photo_url')
