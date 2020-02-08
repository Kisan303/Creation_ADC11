from django.shortcuts import render, redirect
from django.http import *
from django.http import HttpResponse
from .models import ChildEduDonor,PoorDonor,HomeDonor
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.db.models import Q
from .models import Upload
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@require_http_methods(["GET", "POST"])
def log(request):
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
	    return render(request, "account/login.html")


#*** Logout after login is done*******
def logout(request):
	auth.logout(request)
	return redirect('/')

@require_http_methods(["GET", "POST"])
def reg(request):

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
	   			return redirect('account:register')
	   		elif User.objects.filter(email=email).exists():  #email id checking from auth user model
	   			messages.info(request,'email is taken')  #if email exit in auth user model then send error message
	   			return redirect('account:register')

	   		else:	
			    user = User.objects.create_user(username=username, first_name=first_name,last_name= last_name,email=email, password=password)
			    user.save()
			    print('user create')
			    return redirect('account:login')
		   

	   else:
	   	   messages.info(request,'password is no matching')
	   	   return redirect('register')
 
	   return redirect('/')  #home page redirect
		  
	else:
		 
 		return render(request,'account/register.html')


def profile(request):
	return render(request, "account/login.html")

# def index(request):
# 	return render(request, "account/index.html")

@login_required(login_url = '/register')#must be user to be donor
def donateChildEdu(request):
	if request.method =='POST':
	   print(request.POST)
	   full_name = request.POST['full_name']
	   contact = request.POST['contact']
	   address = request.POST ['address']
	   street  = request.POST['street']
	   city = request.POST['city']
	   postal_code = request.POST['postal_code']
	   country = request.POST['country']
	   email= request.POST['email']
	   donate_catagory = request.POST['donate_catagory']
	   donate_amt = request.POST['donate_amt']
	   comments = request.POST['comments']
	   if donate_catagory == 'Child Education':
		   ch1 = ChildEduDonor.objects.create(full_name=full_name,contact= contact,address=address,street=street, city = city, postal_code=postal_code, country=country, donate_catagory=donate_catagory, donate_amt=donate_amt, comments=comments)
		   ch1.save()
	   elif donate_catagory == 'Poor People':
	   	   poor = PoorDonor.objects.create(full_name=full_name,contact= contact,address=address,street=street, city = city, postal_code=postal_code, country=country, donate_catagory=donate_catagory, donate_amt=donate_amt, comments=comments)
	   	   poor.save()
	   		#insert intio database of poor people
	   elif donate_catagory == 'Homeless Person':
	   	   home = HomeDonor.objects.create(full_name=full_name,contact= contact,address=address,street=street, city = city, postal_code=postal_code, country=country, donate_catagory=donate_catagory, donate_amt=donate_amt, comments=comments)
	   	   home.save()
	   		#insert intio database of homeless people
	   return HttpResponse("Donate Successfull!!! thank you")
	else:
 		return render(request,'account/donorform.html')

def dispatch(self, *args, **kwargs):
       return super().dispatch(*args, **kwargs)

def memList(request):
 	return render(request, "account/members.html")

def search(request):
	if request.method=='POST':
		srch=request.POST['srh']
		
		if srch:
			match = ChildEduDonor.objects.filter(Q(full_name__icontains=srch) |
				Q(donate_amt__icontains=srch) | Q(email__icontains=srch))
			if match:
				return render(request, 'account/members.html', {'sr':match})
			else:
				messages.error(request, 'no result found')
		else:
				return HttpResponseRedirect('/search/')
	return render(request, 'account/members.html')


	# last_name=models.CharField(max_length=250)
	# username=models.CharField(max_length=250)
	# contact=models.DateField()
	# address=models.CharField(max_length=50)
	# age=models.IntegerField(10)
	# email=models.EmailField(10)
	# password=models.CharField(max_length=250)
	# confirm_password=models.CharField(max_length=250)
	


def upload(request):

	if request.method == 'POST':
		Title= request.POST['Title']
		Date= request.POST['Date']
		image= request.FILES.get('image')
		Description =request.POST['Description']
		print(image)

		creation = Upload.objects.create(Title=Title, Date=Date, image=image, Description=Description)
		creation.save();
		return redirect('/')

	else:
		return render(request, "account/upload.html")	


def home(request):
	creation2 = Upload.objects.all()	
	print(creation2)
	return render(request, 'account/index.html', {"creation2":creation2})

def upload_list(request):

    query=""
    if request.GET:
        query=request.GET['q']

    images = get_data_queryset(str(query))
    return render(request, "account/uploadlist.html", {"record":images})

def delete_photo(request, pk):
    if request.method=="POST":
        images = Upload.objects.get(pk=pk)
        images.delete()
    return redirect('account:media/images')

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        record = Upload.objects.filter(
            Q(Title__icontains=q) |
            Q(Description__icontains=q)
        )

        for images in record:
            queryset.append(images)
    return list(set(queryset))


