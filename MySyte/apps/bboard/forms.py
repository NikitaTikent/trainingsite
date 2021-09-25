from django.forms import ModelForm
from django import forms
from django.core import validators
from captcha.fields import CaptchaField

from .models import Bboard, Bboard_categories, Img


class BbForm(ModelForm):
	class Meta:
		model = Bboard
		fields = ('title', 'coast', 'description', 'categories')


class SearhForm(forms.Form):
	description = forms.CharField(max_length=30, label='Ключевые слова поиска')
	category = forms.ModelChoiceField(queryset=Bboard_categories.objects.all(), label='Категория')
	captсha = CaptchaField(label='Введите текст с картинки',
		error_messages={'invalid': 'Неправильный текст'})


class ImgForm(forms.ModelForm):
	img = forms.ImageField(label='Изображение',
		validators=[validators.FileExtensionValidator(allowed_extensions=('png', 'jpg'))],
		error_messages={'invalid_extension': 'Этот формат не поддержвается'},
		help_text='Поддерживаемые форматы: png')
	class Meta:
		model = Img
		fields = '__all__'
