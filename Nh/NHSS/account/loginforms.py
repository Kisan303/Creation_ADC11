from django import forms
from .models import Register

class LoginForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ("username", "password")
