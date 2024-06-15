from django import forms
from app.models import Registration


class RegistrationForm(forms.ModelForm):
	class Meta:
		model=Registration
		fields="__all__"