from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from .models import Blog_articles, Blog_comments
from .forms import BlogForms


def index(request):
	articles = Blog_articles.objects.all()
	return render(request, 'blog/blog.html', {'articles':articles})


def article(request, article_id):
	article = Blog_articles.objects.get(id=article_id)
	comments = Blog_comments.objects.filter(article=article)

	if request.method == 'POST':
		Create_new_comment(request)

	return render(request, 'blog/article.html', {'article':article, 'comments': comments})


class Add_article(CreateView):
	"""Класс создания страницы с формой для создания новой статьи"""
	template_name = 'blog/articles_add.html'
	form_class = BlogForms
	success_url = reverse_lazy('blog:index')


def Create_new_comment(request):
	"""Создает новый комментарий для статьи"""
	name = request.POST['name']
	comment = request.POST['comment']
	article_id=request.POST['article_id']
	article = Blog_articles.objects.get(id=article_id)
	Blog_comments(name=name, comment=comment, article=article).save()



class Blog_article(DetailView):
	"""Для сранения функцции и класса для одного и того же вызова"""
	model = Blog_articles
	template_name = 'blog/article.html'	#Можно не использовать, упростил для теста

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		article = Blog_articles.objects.get(pk=context['object'].pk)
		comments = Blog_comments.objects.filter(article=article)
		context['comments'] = comments

		return context

