from django.forms import ModelForm
from .models import Blog_articles

class BlogForms(ModelForm):
	class Meta:
		model = Blog_articles
		fields = ('autor', 'title', 'articles')
