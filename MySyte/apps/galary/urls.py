from django.urls import path
from . import views

app_name = 'galary'

urlpatterns = [
	path('', views.index, name='index'),
	path('add/', views.add, name='add'),
	path('update/<int:pk>', views.Calary_update.as_view(), name='update'),
	path('delete/<int:pk>', views.Galary_delete.as_view(), name='delete')
]
