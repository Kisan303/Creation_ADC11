from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages 
#from .models import Register


def login(request):
	if request.method=='POST':
	   username = request.POST['username']
	   password = request.POST['password'] 

	   user = auth.authenticate(username=username, password=password) # checking user name and password match from auth user model

	   if user is not None:
	   	   auth.login(request, user)
	   	   return redirect('/')

	   else:
	       messages.info(request,'invalid information')
	       return redirect('login')   

	else:
	    return render(request, "registration/login.html")





def register (request):

	if request.method =='POST':

	#***** using djanho auth user model for registraion for database model******	
	   
	   first_name = request.POST['first_name']
	   last_name = request.POST['last_name']

	   username = request.POST ['username']
	   #contact  = request.POST['contact']
	   #address = request.POST['address']
	   #age = request.POST['age']
	   email = request.POST['email']
	   password= request.POST['password']
	   confirm_password = request.POST['confirm_password']

	   if password==confirm_password: #comparing password and confirm password are equal or not
	   		if User.objects.filter(username=username).exists(): #user name checking from auth user model
	   			messages.info(request,'username is taken')  # if user name is exsit already send error message
	   			return redirect('register')
	   		elif User.objects.filter(email=email).exists():  #email id checking from auth user model
	   			messages.info(request,'email is taken')  #if email exit in auth user model then send error message
	   			return redirect('register')

	   		else:	
			    user = User.objects.create_user(username=username, first_name=first_name,last_name= last_name,email=email, password=password)
			    user.save();
			    print('user create')
			    return redirect('login')
		   

	   else:
	   	   messages.info(request,'password is no matching')
	   	   return redirect('register')
 
	   return redirect('/')  #home page redirect
		  
	else:
		 
 		return render(request,'registration/register.html')




def profile(request):
	return render(request, "registration/login.html")

def index(request):
	return render(request, "registration/index.html")
 #    first_name=models.CharField(max_length=250)
	# last_name=models.CharField(max_length=250)
	# username=models.CharField(max_length=250)
	# contact=models.DateField()
	# address=models.CharField(max_length=50)
	# age=models.IntegerField(10)
	# email=models.EmailField(10)
	# password=models.CharField(max_length=250)
	# confirm_password=models.CharField(max_length=250)
	