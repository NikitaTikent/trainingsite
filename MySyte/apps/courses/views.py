from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse

from .models import Course, Student


def index(request):
	courses = Course.objects.all()
	students = Student.objects.all()
	return render(request, 'courses/courses.html', {'courses': courses, 'students': students})
