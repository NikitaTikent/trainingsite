from django.forms import ModelForm
from .models import Galary

class GalaryForms(ModelForm):
	class Meta:
		model = Galary
		fields = ('autor', 'photo_url')
