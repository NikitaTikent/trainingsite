from django.db import models


class Course(models.Model):
	name = models.CharField('Название курса', max_length=100)


class Student(models.Model):
	name = models.CharField('Имя студента', max_length=80)
	courses = models.ManyToManyField(Course)