from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
	path('', views.index, name='index'),
	path('student_courses/<int:pk>/', views.student_courses, name='student_courses'),
	path('course_students/<int:pk>/', views.course_students, name='course_students')
]
