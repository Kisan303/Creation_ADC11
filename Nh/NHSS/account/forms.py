from django import forms
from .models import Register

class LoginForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ("username", "password")

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = ("first_name","last_name","username","contact", "address", "age", "email", "password", "confirm_password")

