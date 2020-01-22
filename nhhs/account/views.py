from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import  auth
from .models import register
def register (request):

	if request.method =='POST':
	   print(request.POST)
	   first_name = request.POST['first_name']
	   last_name = request.POST['last_name']

	   username = request.POST ['username']
	   contact  = request.POST['contact']
	   address = request.POST['address']
	   age = request.POST['age']
	   email = request.POST['email']
	   password= request.POST['password']
	   confirm_password = request.POST['confirm_password']
	   r1 = register(first_name=first_name,last_name= last_name,username=username,contact=contact, address = address, age=age, email=email, password=password, confirm_password=confirm_password)
	   r1.save()
	   return HttpResponse("Test")
	else:
 		return render(request,'registration/register.html')
 #    first_name=models.CharField(max_length=250)
	# last_name=models.CharField(max_length=250)
	# username=models.CharField(max_length=250)
	# contact=models.DateField()
	# address=models.CharField(max_length=50)
	# age=models.IntegerField(10)
	# email=models.EmailField(10)
	# password=models.CharField(max_length=250)
	# confirm_password=models.CharField(max_length=250)
	