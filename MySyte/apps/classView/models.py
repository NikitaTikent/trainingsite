from django.db import models

class test(models.Model):
	name = models.CharField('Имя', max_length=100)
	age = models.IntegerField('Возраст')
	date = models.DateTimeField('Дата регистрации', auto_now_add=True)

	class Meta:
		verbose_name = 'Для теста класса view'
