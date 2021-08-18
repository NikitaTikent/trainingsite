from django.urls import path
from . import views


app_name = 'bank'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:user_id>', views.user_cards, name='user_cards'),
	path('car_details/<int:car_id>', views.car_details, name='car_details')
]
