from django.urls import path
from . import views

app_name = 'bboard'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:categori_id>', views.sorting, name='sorting'),
	path('add/', views.BbCreateView.as_view(), name='add'),
	path('bboard_update/<int:pk>', views.Bboard_update.as_view(), name='update'),
	path('delete/<int:pk>', views.Bboard_delete.as_view(), name='delete'),
	path('bboard_and_categories/<int:category_id>', views.bboard_and_categories, name='bboard_and_categories'),
	path('searh/', views.bboard_searh, name='searh'),
	path('add/img/', views.add_img, name='add_img'),
	path('delete/img/<int:img_pk>', views.delete_img, name='delete_img')
]
