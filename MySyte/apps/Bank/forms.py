from django.forms import ModelForm
from .models import User

class BankForm(ModelForm):
	class Meta:
		model = User
		fields = ('name', 'cards_number')
