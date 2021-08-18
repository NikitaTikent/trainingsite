from django.db import models


class Card(models.Model):
	number = models.PositiveIntegerField('Номер карты')

	def __str__(self):
		return str(self.number)

	class Meta:
		verbose_name = 'Номер карты'
		verbose_name_plural = 'Номера карты'

class User(models.Model):
	name = models.CharField('Имя пользователя', max_length=80)
	cards_number = models.ManyToManyField(Card, verbose_name='Номера карт')

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

############### next models only for an experience in shell

class Details(models.Model):
	name = models.CharField('Название детали', max_length=80)
	coast = models.FloatField('Цена детали')
	color = models.CharField('Цвет детали', max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Деталь'
		verbose_name_plural = 'Детали'


class Cars(models.Model):
	name = models.CharField('Название машины', max_length=50)
	details = models.ManyToManyField(Details)
	color = models.CharField('Цвет машины', max_length=80)
	coast = models.FloatField('Цена Машины')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Машина'
		verbose_name_plural = 'Машины'


############

class Student(models.Model):
	name = models.CharField('Имя студента', max_length=100)
	age = models.PositiveSmallIntegerField('Возраст')


class Course(models.Model):
	name = models.CharField('Название курса', max_length=100)
	students = models.ManyToManyField(Student)
	coast = models.FloatField('Цена курса')
