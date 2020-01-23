from django.db import models

# Create your models here.
class Register(models.Model):
	first_name=models.CharField(max_length=250)
	last_name=models.CharField(max_length=250)
	username=models.CharField(max_length=250)
	contact=models.IntegerField()
	address=models.CharField(max_length=50)
	age=models.IntegerField()
	email=models.EmailField(max_length=150)
	password=models.CharField(max_length=250)
	confirm_password=models.CharField(max_length=250)

	
	def __str__(self):
		return self.first_name
