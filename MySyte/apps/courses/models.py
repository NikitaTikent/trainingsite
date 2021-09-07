from django.db import models


class Course(models.Model):
	name = models.CharField('Название курса', max_length=100)

	def __str__(self):
		return str(self.name)
	
	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'


class Student(models.Model):
	name = models.CharField('Имя студента', max_length=80)
	courses = models.ManyToManyField(Course)

	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name="Студент"
		verbose_name_plural="Студенты"