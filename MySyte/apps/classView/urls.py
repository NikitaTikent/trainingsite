from django.urls import path
from . import views

app_name = 'classView'

urlpatterns = [
	path('', views.index, name='index'),
	path('age_choise/<int:pk>', views.NameClassView.as_view(), name='test_class')
]
