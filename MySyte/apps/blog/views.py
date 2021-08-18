from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Blog_articles, Blog_comments
from .forms import BlogForms


def index(request):
	articles = Blog_articles.objects.all()
	return render(request, 'blog/blog.html', {'articles':articles})


def article(request, article_id):
	article = Blog_articles.objects.get(id=article_id)
	comments = Blog_comments.objects.filter(article=article)
	return render(request, 'blog/article.html', {'article':article, 'comments': comments})

def new_comment(request):
	articles = Blog_articles.objects.all()
	Create_new_comment(request)
	return render(request, 'blog/blog.html', {'articles':articles})



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

