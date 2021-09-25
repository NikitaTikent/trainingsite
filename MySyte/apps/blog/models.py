from django.db import models


class Blog_articles(models.Model):
	"""Статьи"""
	autor = models.CharField('Автор', max_length=100)
	title = models.CharField('Название статьи', max_length=200)
	articles = models.TextField('Статьи')
	date = models.DateTimeField('Дата публикации', auto_now_add=True)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


class articles_autor(Blog_articles):
	"""Сортировка по автору"""

	class Meta:
		proxy = True
		ordering = ['-autor']

class Blog_comments(models.Model):
	"""Комментарии к статье"""
	name = models.CharField('Имя автора', max_length=100)
	comment = models.TextField('комментарий')
	date = models.DateTimeField('Дата', auto_now_add=True)
	article = models.ForeignKey(Blog_articles, on_delete=models.CASCADE, null=True, verbose_name='Статья')

	def __str__(self):
		return str(self.article)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
