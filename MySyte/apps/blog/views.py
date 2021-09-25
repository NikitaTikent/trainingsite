from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Blog_articles, Blog_comments
from .forms import BlogForms, CommentSearh


def index(request):
	articles = Blog_articles.objects.all()
	context = {'articles':articles}

	return render(request, 'blog/blog.html', context)


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
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		article = Blog_articles.objects.get(pk=context['object'].pk)
		comments = Blog_comments.objects.filter(article=article)
		context['comments'] = comments

		return context


class Article_update(UpdateView):
	model = Blog_articles
	template_name = 'blog/articles_add.html'
	models_form = BlogForms
	fields = ('autor', 'title', 'articles')
	success_url = '/blog/{id}'


class Article_delete(DeleteView):
	model = Blog_articles
	template_name = 'blog/article_delete.html'
	success_url = '/blog'


def comment_searh(request):
	if request.method == 'POST':
		scf = CommentSearh(request.POST)
		if scf.is_valid():
			keyword = scf.cleaned_data['keyword']
			article = scf.cleaned_data['article']
			searh_res = Blog_comments.objects.filter(comment__icontains=keyword, article=article)
			context = {'searh_res': searh_res}
	else:
		searh_form = CommentSearh()
		context = {'form': searh_form}
	
	return render(request, 'blog/comment_searh.html', context)
