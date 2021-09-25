from django.db import models
from datetime import datetime


class Bboard_categories(models.Model):
	categories = models.CharField('Категории', max_length=200)
	
	def __str__(self):
		return self.categories

	class Meta:
		verbose_name = 'Категории'
		verbose_name_plural = 'Категории'


class Bboard(models.Model):
	title = models.CharField('Заголовок', max_length=150)
	coast = models.FloatField('Цена')
	description = models.TextField('Описание')
	categories = models.ForeignKey(Bboard_categories, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Объявление'
		verbose_name_plural = 'Объявления'


def get_src_img(instance, filename):
	return '%d%s'%(datetime.now().timestamp(), filename)


class Img(models.Model):
	img = models.ImageField(upload_to=get_src_img, verbose_name='Изображение')
	description = models.TextField(verbose_name='Описание')

	def delete(self, *args, **kwargs):
		self.img.delete(save=False)
		super().delete(*args, **kwargs)

	class Meta:
		verbose_name = 'Изображение'
		verbose_name_plural = 'Изображения'
