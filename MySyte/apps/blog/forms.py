from django.forms import ModelForm
from django import forms
from .models import Blog_articles

class BlogForms(ModelForm):
	class Meta:
		model = Blog_articles
		fields = ('autor', 'title', 'articles')


class CommentSearh(forms.Form):
	keyword = forms.CharField(max_length=30, label='Ключевое слово')
	article = forms.ModelChoiceField(queryset=Blog_articles.objects.all(),
		label='Статья')
