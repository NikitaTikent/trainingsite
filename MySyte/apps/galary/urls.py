from django.urls import path
from . import views

app_name = 'galary'

urlpatterns = [
	path('', views.index, name='index'),
	path('add/', views.add, name='add'),
	path('test', views.Galary_info.as_view(), name='test'),
	path('update/<int:pk>', views.Calary_update.as_view(), name='update')
]
