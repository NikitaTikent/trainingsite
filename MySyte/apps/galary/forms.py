from django import forms
from django.core import validators

from .models import Galary

class GalaryForms(forms.ModelForm):
	class Meta:
		model = Galary
		fields = ('autor', 'photo_url')


class Galary_detail(forms.ModelForm):
	autor = forms.CharField(label='Имя автора', 
		validators=[validators.RegexValidator(regex='admin')],
		error_messages={'invalid': 'Неправильно имя'})
	
	photo_url = forms.CharField(label='Сылка на фото')
	age = forms.IntegerField(label='Возраст')
	choices_test = forms.MultipleChoiceField(label='Тест выбора',choices=(
		('a', 'first'),
		('b', 'second'),
		('c', 'third')
		))
	publication_date = forms.DateField(label='Выберите дату публикации', 
						widget = forms.widgets.SelectDateWidget()
						)
	password = forms.CharField(label='Пароль', widget = forms.widgets.PasswordInput())

	class Meta:
		model = Galary
		fields = ('autor', 'photo_url')
