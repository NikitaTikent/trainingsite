from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>', views.Blog_article.as_view(), name='article'),
	path('new_comment/<int:article_id>', views.article, name='new_comment'),
	path('add/', views.Add_article.as_view(), name='add_article'),
	path('update/<int:pk>', views.Article_update.as_view(), name='update'),
	path('delete/<int:pk>', views.Article_delete.as_view(), name='delete'),
	path('comment_searh/', views.comment_searh, name='comment_searh')
]
