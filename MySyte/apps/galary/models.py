from django.contrib.contenttypes.fields import GenericRelation

from django.db import models
from user.models import Note

class Galary(models.Model):
	autor = models.CharField('Имя автора', max_length=100)
	photo_url = models.TextField('Ссылка на фотографию')
	date = models.DateTimeField('Дата публикации', auto_now_add=True)
	order = models.SmallIntegerField(default=0, db_index=True)

	note = GenericRelation(Note)
	
	def __str__(self):
		return self.autor

	class Meta:
		verbose_name = 'Галерея'
		verbose_name_plural = 'Галерея'
		ordering = ['order', 'autor']




class Galary_fasttest(models.Model):
	KIND = (
		('a', 'Куплю'),
		('c', 'продам'),
		('b', 'обменяю'),
		)
	
	kind = models.CharField(max_length=1, choices=KIND, default='s')
	text = models.TextField('Текст', null=True)

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Галерея_test'
		verbose_name_plural = 'Галерея_test'
