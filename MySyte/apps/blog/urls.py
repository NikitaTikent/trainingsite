from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	#path('<int:article_id>', views.article, name='article'),
	path('<int:pk>', views.Blog_article.as_view(), name='article'),
	path('new_comment', views.article, name='new_comment'),
	path('add/', views.Add_article.as_view(), name='add_article')
]
