from django.urls import path
from . import views

app_name = 'bboard'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:categori_id>', views.sorting, name='sorting'),
	path('add/', views.BbCreateView.as_view(), name='add')
]
