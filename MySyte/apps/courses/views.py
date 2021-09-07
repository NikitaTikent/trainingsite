from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse

from .models import Course, Student


def index(request):
	courses = Course.objects.all()
	students = Student.objects.all()
	return render(request, 'courses/courses.html', {'courses': courses, 'students': students})


def student_courses(request, pk):
	student = Student.objects.get(pk=pk)
	return render(request, 'courses/student_courses.html', {'student': student,})


def course_students(request, pk):
	course = Course.objects.get(pk=pk)
	return render(request, 'courses/course_students.html', {'course': course})
